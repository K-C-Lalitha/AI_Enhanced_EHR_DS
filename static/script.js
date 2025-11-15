document.getElementById('processBtn').addEventListener('click', async () => {
  const image = document.getElementById('imageUpload').files[0];
  if (!image) return alert('⚠️ Please upload an image.');

  const formData = new FormData();
  formData.append('image', image);

  try {
    const btn = document.getElementById('processBtn');
    btn.textContent = 'Processing...';
    btn.disabled = true;

    const res = await fetch('/upload_image', { method: 'POST', body: formData });
    const data = await res.json();

    if (data.error) {
      alert(data.error);
      return;
    }

    
    document.getElementById('originalImage').src = '/' + data.original_path;
    document.getElementById('enhancedImage').src = '/' + data.enhanced_path;

   
    const formattedNote = data.note
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*   /g, '• ')
      .replace(/\n/g, '<br>');

    document.getElementById('clinicalNote').innerHTML = formattedNote;
  } catch (err) {
    console.error(err);
    alert('❌ Error processing the image.');
  } finally {
    const btn = document.getElementById('processBtn');
    btn.textContent = 'Process Image';
    btn.disabled = false;
  }
});
