// On Vercel the API is on the same domain — no need for an absolute URL.
// "/api/fill-form" works both locally (if you run vercel dev) and in production.
const API_URL = "/api/fill-form";

function previewPhoto(event) {
  const file = event.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = e => {
    document.getElementById('photoPreview').src = e.target.result;
  };
  reader.readAsDataURL(file);
}

document.getElementById('mentorForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const btn = document.getElementById('submitBtn');
  const msg = document.getElementById('statusMsg');

  btn.disabled    = true;
  btn.textContent = '⏳ Generating Excel…';
  msg.textContent = '';
  msg.className   = '';

  try {
    const formData = new FormData(this);

    const response = await fetch(API_URL, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      const errText = await response.text();
      throw new Error(errText || `Server error ${response.status}`);
    }

    const blob = await response.blob();
    const url  = window.URL.createObjectURL(blob);
    const a    = document.createElement('a');
    a.href     = url;

    // Extract filename from Content-Disposition header if available
    const cd = response.headers.get('Content-Disposition') || '';
    const match = cd.match(/filename="?([^"]+)"?/);
    a.download = match ? match[1] : 'Mentor-Mentee-Form.xlsx';

    document.body.appendChild(a);
    a.click();
    a.remove();
    window.URL.revokeObjectURL(url);

    msg.textContent = '✅ Excel downloaded successfully!';
    msg.className   = 'success';

  } catch (err) {
    msg.textContent = '❌ Error: ' + err.message;
    msg.className   = 'error';
  } finally {
    btn.disabled    = false;
    btn.textContent = '📥 Submit & Download Excel';
  }
});
