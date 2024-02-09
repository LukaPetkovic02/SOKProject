
window.onload = function() {
    function copySVG() {
        var containerMain=document.getElementById('graph_svg');
        var originalSVG = document.getElementById('graph_svg');
        var copiedSVGContainer = document.getElementById('bird_view_container');

        // Clone the original SVG element
        var copiedSVG = originalSVG.cloneNode(true);

        w=containerMain.clientWidth;
        h=containerMain.clientHeight

        birdViewHeight=5000
        birdViewWidth=5000

        var offsetX = (w - birdViewHeight) / 2;
        var offsetY = (h - birdViewWidth) / 2;


        copiedSVG.setAttribute('viewBox', offsetX+' '+offsetY+' '+birdViewWidth+' '+birdViewHeight);


        // Remove the ID attribute to prevent duplicate IDs
        copiedSVG.removeAttribute('id');


        var viewBoxParams = originalSVG.viewBox.baseVal;
        var rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        // Set attributes for the rectangle
        rect.setAttribute('x', viewBoxParams.x);
        rect.setAttribute('y', viewBoxParams.y);
        rect.setAttribute('width', viewBoxParams.width);
        rect.setAttribute('height', viewBoxParams.height);
        rect.setAttribute('fill', 'none');
        rect.setAttribute('stroke', 'red'); // Set stroke color
        rect.setAttribute('stroke-width', '20'); // Set stroke width

        // Append the rectangle to the copied SVG
        copiedSVG.appendChild(rect);

        // Remove any existing SVG content in the copied container
        copiedSVGContainer.innerHTML = '';

        // Append the cloned SVG to the copied container
        copiedSVGContainer.appendChild(copiedSVG);
    }

    // Call the function to copy SVG initially
    copySVG();
  // Start observing the target SVG for attribute changes
  setInterval(copySVG, 500);
}
