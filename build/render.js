// passage_v.html を PDF に変換する: node build/render.js
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const src = path.join(__dirname, 'passage_v.html');
  const out = path.join(__dirname, '..', 'english_passage_V_solution.pdf');
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + src);
  await page.pdf({
    path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;text-align:center;font-size:8pt;color:#666"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
  });
  await browser.close();
  console.log('wrote', out);
})();
