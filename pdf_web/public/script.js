document.getElementById('sendBtn').addEventListener('click', async () => {
  const raw = document.getElementById('jsonInput').value;
  let aiData;
  try {
    aiData = JSON.parse(raw);
  } catch (e) {
    alert('请确保输入的是合法的 JSON');
    return;
  }

  const res = await fetch('/api/report/pdf', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(aiData)
  });

  // 如果返回 PDF，则下载；否则展示返回的 JSON
  if (res.ok && res.headers.get('content-type').includes('application/pdf')) {
    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'AI_Report.pdf';
    document.body.appendChild(a);
    a.click();
    a.remove();
    window.URL.revokeObjectURL(url);
  } else {
    const data = await res.json();
    document.getElementById('result').textContent = JSON.stringify(data, null, 2);
  }
});
