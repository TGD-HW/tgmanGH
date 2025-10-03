document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('img.viewer-skip').forEach(img => {
        // 1. Glightbox Cleanup
        img.removeAttribute('data-glightbox');
        img.classList.remove('glightbox');
        const parent = img.parentElement;
        if (parent && parent.tagName === 'A' && parent.classList.contains('glightbox')) {
            // Unwrap the image from the 'a' tag
            parent.replaceWith(img); 
        }

        // 2. Initialize Viewer.js directly on the <img> element
        const viewer = new Viewer(img, {
            inline: true,
            toolbar: false,
            navbar: false,
            title: false,
            zoomRatio: 0.2, 
            minZoomRatio: 0.1,
            maxZoomRatio: 5,
            transition: false,
            movable: true,
            zoomable: true,
            scalable: false,
            rotatable: false,
            url: 'src',

            // CRITICAL: Once the Viewer is ready and its DOM is built:
            ready: function() {
                // Get the main Viewer element which is created *around* the image
                const viewerElement = this.viewer; // This is the Viewer.js container (usually a div)

                // Add the custom styling class to the Viewer's container element
                viewerElement.classList.add('viewer-container');
                
                // IMPORTANT: The original <img> is now a sibling of the Viewer element.
                // We must remove the *original* <img> element to eliminate its reserved space.
                if (img) {
                    img.remove();
                }
            }
        });
    });
});