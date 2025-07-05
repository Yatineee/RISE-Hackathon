# 📊 Weekly AI Report

This project uses **Node.js** and **EJS** templates to render a simple “Weekly AI Report” page.

## Directory Structure

```
your-project/
├── public/          # Static assets (logo, CSS, JS, etc.)
│   └── logo.png
├── views/           # EJS templates
│   └── index.ejs
├── server.js        # Entry script
├── package.json     # npm dependencies and scripts
└── README.md        # Project documentation (this file)
```

## Prerequisites

* **Node.js** v14 or higher
* **npm** (included with Node.js)

## Dependencies

This project relies on the following npm packages:

* express
* body-parser
* ejs
* puppeteer

## Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-org/your-project.git
   cd your-project
   ```

2. **Install dependencies**

   ```bash
   npm install
   # (Installs express, body-parser, ejs, puppeteer as specified in package.json)
   ```

   If you don't have the dependencies in `package.json`, run:

   ```bash
   npm install express body-parser ejs puppeteer
   ```

3. **Start the server**

   ```bash
   node server.js
   ```

   Open your browser and go to `http://localhost:3001/`.

## Common Scripts

* `node server.js`
  Launch the Node.js server (default port: 3001).
* `npm run dev`
  (Optional) Start in development mode with automatic reload. Add this script to `package.json` as needed.

## Environment Variables

Configure the port or other settings by creating a `.env` file in the project root:

```
PORT=3001
```

Environment variables will be loaded automatically (requires `dotenv` in `package.json`).

---

> **Tip:**
>
> * Use `nvm` to manage Node.js versions.
> * If the port is already in use, update the `.env` file or the `server.js` file accordingly.
> * EJS template files are in `views/index.ejs`; static assets are in `public/`.
