document.addEventListener("DOMContentLoaded", function() {
    var banner = document.createElement('div');
    banner.id = "archive-notice";
    banner.innerHTML = `
        <div style="background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; padding: 15px; margin: 20px; border-radius: 4px; font-family: sans-serif;">
            <h2 style="margin-top: 0;">ℹ️ Project archival notice</h2>
            <p>Thank you to everyone who has used, tested, and contributed to this project. Due to lack of time, I will archive the repository: it will be archived and no longer actively maintained as of <strong>April 1</strong>.</p>
            <ul>
                <li>New issues and pull requests will not be answered after that date.</li>
                <li>I will publish a final release on March 31; that will be the last release.</li>
            </ul>
            <p>If you would like to take over the project, have questions, or need to communicate anything related to it, please contact me at <a href="mailto:isaaker@piscinadeentropia.es" style="color: #533f03; font-weight: bold;">isaaker@piscinadeentropia.es</a>.</p>
        </div>
    `;

    // Inserta el banner al principio del contenedor principal
    var container = document.querySelector('.md-container') || document.body;
    container.prepend(banner);
});
