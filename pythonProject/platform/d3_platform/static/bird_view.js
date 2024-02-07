
window.onload = function() {
    function copySVG() {
        var container=document.getElementById('graph_svg');
        var containerMain=document.getElementById('graph_svg');
        var originalSVG = document.getElementById('graph_svg');
        var copiedSVGContainer = document.getElementById('bird_view_container');

        // Clone the original SVG element
        var copiedSVG = originalSVG.cloneNode(true);

        w=containerMain.clientWidth;
        h=containerMain.clientHeight


        var offsetX = (w - 3000) / 2;
        var offsetY = (h - 3000) / 2;


        copiedSVG.setAttribute('viewBox', offsetX+' '+offsetY+' '+3000+' 3000');


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

    // Update the copied SVG whenever the original SVG changes

      function handleAttributeChanges(mutationsList, observer) {
    mutationsList.forEach(mutation => {
      if (mutation.type === 'attributes' && isInsideSvg(mutation.target)) {
        copySVG()
      }
    });
  }

  // Function to check if an element or any of its ancestors is an SVG element
  function isInsideSvg(element) {
    while (element) {
      if (element.tagName === 'svg' || element.tagName === 'SVG') {
        return true;
      }
      element = element.parentNode;
    }
    return false;
  }

  // Select the target SVG element
  const targetSvg = document.getElementById('graph_svg');

  // Create a MutationObserver to watch for changes to attributes
  const observer = new MutationObserver(handleAttributeChanges);

  // Configure the MutationObserver to observe changes in attributes of the target SVG or its children
  const config = { attributes: true, subtree: true };

  // Start observing the target SVG for attribute changes
  observer.observe(targetSvg, config);
}
