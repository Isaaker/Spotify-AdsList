app.document$.subscribe(function() {
  var container = document.querySelector('.md-container');
  
  if (container && !document.getElementById("archive-notice")) {
    
    var banner = document.createElement('div');
    banner.id = "archive-notice";
    
    banner.innerHTML = `
        <div style="background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; padding: 20px; margin: 20px; border-radius: 8px; font-family: sans-serif; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h2 style="margin-top: 0; color: #856404;">ℹ️ Project archival notice</h2>
            <p>Thank you to everyone who has used, tested, and contributed to this project. Due to lack of time, I will archive the repository as of <strong>April 1</strong>.</p>
            <ul style="margin-bottom: 15px;">
                <li>New issues and pull requests will not be answered after that date.</li>
                <li>I will publish a final release on March 31.</li>
            </ul>
            <p>Questions? Contact: <a href="mailto:isaaker@piscinadeentropia.es" style="color: #533f03; font-weight: bold; text-decoration: underline;">isaaker@piscinadeentropia.es</a></p>
        </div>
    `;

    container.prepend(banner);
  }
});
