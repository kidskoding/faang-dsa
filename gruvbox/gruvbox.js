(function() {
    'use strict';

    function removeOnThisPageSidebar() {
        document.querySelectorAll('#mdbook-sidebar .on-this-page').forEach(function(node) {
            node.remove();
        });
    }

    document.addEventListener('DOMContentLoaded', function() {
        removeOnThisPageSidebar();
        window.setTimeout(removeOnThisPageSidebar, 0);
    });

    var btn = document.getElementById('mdbook-theme-default_theme');
    if (btn) {
        btn.textContent = 'Gruvbox';
    }
})();
