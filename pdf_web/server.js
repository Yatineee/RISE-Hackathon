// server.js
const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const ejs = require('ejs');
const puppeteer = require('puppeteer');


const app = express();
app.use(bodyParser.json());
// 把 public 下的文件都当静态资源
app.use('/public', express.static(path.join(__dirname, 'public')));

// 配置 EJS 模板目录 Configure the EJS template directory
app.set('views', path.join(__dirname, 'templates'));
app.set('view engine', 'ejs');

// Provide front-end static files
app.use('/', express.static(path.join(__dirname, 'public')));

// 生成 PDF 接口 Generate PDF interface
app.post('/api/report/pdf', async (req, res) => {
  try {
    const aiData = req.body;
    // 渲染 HTML  Render HTML
    const html = await ejs.renderFile(
      path.join(__dirname, 'templates', 'report.ejs'),
      aiData,
      { async: true }
    );
    const browser = await puppeteer.launch({
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    await page.setContent(html, { waitUntil: 'networkidle0' });
    const pdfBuffer = await page.pdf({
      format: 'A4',
      printBackground: true,
      margin: { top: '20px', bottom: '20px', left: '20px', right: '20px' }
    });
    await browser.close();
    // 返回 PDF
    res.set({
      'Content-Type': 'application/pdf',
      'Content-Disposition': 'attachment; filename=AI_Report.pdf'
    });
    res.send(pdfBuffer);
  } catch (err) {
    console.error('PDF 生成失败', err);
    res.status(500).json({ error: 'PDF 生成失败' });
  }
});

// 健康检查
app.get('/api/health', (req, res) => res.json({ status: 'ok' }));

// 启动服务
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`✅ Server listening on http://localhost:${PORT}`);
});
