// -------------------------------------------------------
// Change this to your deployed backend URL after deploying
// e.g. "https://mentor-mentee-api.onrender.com"
// -------------------------------------------------------
const API_URL = "http://localhost:8000";

function previewPhoto(event) {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = e => {
      document.getElementById('photoPreview').src = e.target.result;
    };
    reader.readAsDataURL(file);
  }
}

document.getElementById('mentorForm').addEventListener('submit', async function(e) {
  e.preventDefault();

  const btn = document.getElementById('submitBtn');
  const msg = document.getElementById('statusMsg');

  btn.disabled = true;
  btn.textContent = '⏳ Generating Excel...';
  msg.textContent = '';
  msg.className = '';

  const formData = new FormData(this);

  try {
    const response = await fetch(`${API_URL}/fill-form`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      const err = await response.text();
      throw new Error(err || 'Server error');
    }

    // Trigger file download
    const blob = await response.blob();
    const url  = window.URL.createObjectURL(blob);
    const a    = document.createElement('a');
    a.href     = url;
    a.download = 'Mentor-Mentee-Form.xlsx';
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
