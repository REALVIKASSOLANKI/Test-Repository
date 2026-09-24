const init = async () => {
  const header = document.querySelector('h1');
  
  header?.addEventListener('click', () => {
    header.textContent = 'Status: Active 🚀';
    console.log(`Session ID: ${globalThis.crypto?.randomUUID()}`);
  });
};

await init();
