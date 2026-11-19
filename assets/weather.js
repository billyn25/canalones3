for (const panel of document.querySelectorAll('[data-forecast]')) {
  panel.hidden = false;
  panel.addEventListener('toggle', () => {
    const output = panel.querySelector('.weather-output');
    if (!panel.open) {
      output.replaceChildren();
      return;
    }
    const frame = document.createElement('iframe');
    frame.title = panel.querySelector('summary').textContent;
    frame.referrerPolicy = 'no-referrer';
    frame.src = panel.dataset.forecast;
    output.replaceChildren(frame);
  });
}
