from api.model.abstract.Visualizer import Visualizer

class SimpleVisualizer(Visualizer):
    def generate_graph(self, graph):
        if graph.directed:
            return generate_directed_graph(graph)
        else:
            return generate_undirected_graph(graph)

    def generate_directed_graph(self, graph):
        # Start the string with the JavaScript code to create the graph
        graph_string = "<script>"
        graph_string += "var nodes = ["

        # Add nodes to the JavaScript representation
        for node in graph.nodes.values():
            graph_string += "{id: '" + str(node.id) + "', name: '" + str(node.name) + "'},"
        graph_string += "];"

        # Add edges to the JavaScript representation
        graph_string += "var links = ["
        for edge in graph.edges.values():

            if edge.node1 != edge.node2:
                reverse_edge_exists = False

                for e in graph.edges.values():
                    if e.node1 == edge.node2 and e.node2 == edge.node1:
                        reverse_edge_exists = True
                        break
                if not reverse_edge_exists:
                    graph_string += "{source: '" + str(edge.node1.id) + "', target: '" + str(edge.node2.id) + "'},"
                else:
                    graph_string += "{source: '" + str(edge.node1.id) + "', target: '" + str(
                        edge.node2.id) + ", curved: true'},"

        graph_string += "];"

        graph_string += "];"

        # Add self-loops to the JavaScript representation
        graph_string += "var selfLoops = ["
        for node in graph.nodes.values():
            # Include only self-loops
            if any(edge.node1 == node and edge.node2 == node for edge in graph.edges.values()):
                graph_string += "{id: '" + str(node.id) + "'},"
        graph_string += "];"

        # Add JavaScript code to create the graph visualization
        graph_string += """
            var width = 960,
                height = 600;

            var svg = d3.select("body").append("svg")
                .attr("width", width)
                .attr("height", height);

            // Force Simulation
            var simulation = d3.forceSimulation(nodes.concat(selfLoops))
                .force("link", d3.forceLink(links).id(d => d.id).distance(function(d) { return 150; })) // Set the desired distance between nodes
                .force("charge", d3.forceManyBody().strength(-200)) // Set a low repulsion force
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("x", d3.forceX(width / 2).strength(0.05))
                .force("y", d3.forceY(height / 2).strength(0.05));

            // Arrowhead Definition
            var marker = svg.append("defs").append("marker")
                .attr("id", "arrowhead")
                .attr("viewBox", "-0 -5 10 10")
                .attr("refX", 35)
                .attr("refY", 0)
                .attr("orient", "auto")
                .attr("markerWidth", 8)
                .attr("markerHeight", 8)
                .attr("xoverflow", "visible");
            marker.append("svg:path")
                .attr("d", "M 0,-5 L 10 ,0 L 0,5")
                .attr("fill", "#999");

            // Link Creation
            var link = svg.append("g")
                .attr("stroke", "#999")
                .attr("stroke-opacity", 0.6)
                .selectAll("path")
                .data(links)
                .enter().append("path")
                .attr("stroke-width", 1)  // Adjust stroke width as needed
                .attr("marker-end", "url(#arrowhead)")
                .attr("fill", "none")
                .attr("class", "link")
                .attr("id", function(d, i) { return "link" + i; })
                .attr("curved", function(d) { return d.curved ? "true" : "false"; });

            // Self-loop Creation
            var selfLoop = svg.append("g")
                .attr("fill", "none")
                .attr("stroke", "#999")
                .attr("stroke-opacity", 0.6)
                .selectAll("path")
                .data(selfLoops)
                .enter().append("path")
                .attr("class", "self-loop")
                .attr("d", function(d) { 
                  var node = nodes.find(node => node.id === d.source);
                  var r = 20; // Node radius
                  var x = node.x;
                  var y = node.y;
                  return "M " + (x + r) + "," + y + " A " + (r*1.5) + "," + (r*1.5) + " 0 1,0 " + (x - r) + "," + y; // Dynamically calculate the self-loop path
                });

            // Node Creation
            var node = svg.append("g")
                .attr("stroke", "#fff")
                .attr("stroke-width", 1.5)
              .selectAll("circle")
              .data(nodes)
              .enter().append("circle")
                .attr("r", 20)  // Adjust the radius of the circle to make it bigger
                .attr("fill", "#000")
                // Add drag behavior to nodes
                .call(d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended));

            // Text inside the Circle
            var text = svg.append("g").selectAll("text")
              .data(nodes)
              .enter().append("text")
                .text(function(d) { return d.name; })
                .attr("fill", "#fff")  // Set text color
                .attr("font-size", "12px")  // Set text font size
                .attr("text-anchor", "middle")  // Center the text horizontally
                .attr("dy", ".35em");  // Adjust vertical alignment of text

            // Tooltip Creation
            node.append("title")
                .text(d => d.name);

            // Simulation Event
            simulation.on("tick", () => {
                link.attr("d", function(d) {
                    if (d.curved) {
                        var dx = d.target.x - d.source.x,
                            dy = d.target.y - d.source.y,
                            dr = Math.sqrt(dx * dx + dy * dy);
                        return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
                    } else {
                        return "M" + d.source.x + "," + d.source.y + "L" + d.target.x + "," + d.target.y;
                    }
                });

                selfLoop
                    .attr("d", function(d) { 
                      var node = nodes.find(node => node.id === d.source);
                      var r = 20; // Node radius
                      var x = node.x;
                      var y = node.y;
                      return "M " + (x + r) + "," + y + " A " + (r*1.5) + "," + (r*1.5) + " 0 1,0 " + (x - r) + "," + y; // Dynamically calculate the self-loop path
                    });

                node
                    .attr("cx", d => d.x)
                    .attr("cy", d => d.y);

                // Update text position with nodes
                text
                    .attr("x", function(d) { return d.x; })
                    .attr("y", function(d) { return d.y; });
            });

            // Drag functions
            function dragstarted(d) {
                if (!d3.event.active) simulation.alphaTarget(0.3).restart();
                d.fx = d.x;
                d.fy = d.y;
            }

            function dragged(d) {
                d.fx = d3.event.x;
                d.fy = d3.event.y;
            }

            function dragended(d) {
                if (!d3.event.active) simulation.alphaTarget(0);
                d.fx = null;
                d.fy = null;
            }
            """
        graph_string += "</script>"

        return graph_string

    def generate_undirected_graph(self, graph):
        # Start the string with the JavaScript code to create the graph
        graph_string = "<script>"
        graph_string += "var nodes = ["

        # Add nodes to the JavaScript representation
        for node in graph.nodes.values():
            graph_string += "{id: '" + str(node.id) + "', name: '" + str(node.name) + "'},"
        graph_string += "];"

        # Add links to the JavaScript representation
        graph_string += "var links = ["
        for edge in graph.edges.values():
            # Exclude self-loops from regular links
            if edge.node1 != edge.node2:
                graph_string += "{source: '" + str(edge.node1.id) + "', target: '" + str(edge.node2.id) + "'},"
        graph_string += "];"

        # Add self-loops to the JavaScript representation
        graph_string += "var selfLoops = ["
        for node in graph.nodes.values():
            # Include only self-loops
            if any(edge.node1 == node and edge.node2 == node for edge in graph.edges.values()):
                graph_string += "{source: '" + str(node.id) + "', target: '" + str(node.id) + "'},"
        graph_string += "];"

        # Add JavaScript code to create the graph visualization
        graph_string += """
            // SVG Initialization
            var width = 960,
                height = 600;

            var svg = d3.select("body").append("svg")
                .attr("width", width)
                .attr("height", height);

            // Force Simulation
            var simulation = d3.forceSimulation(nodes.concat(selfLoops))
                .force("link", d3.forceLink(links).id(d => d.id).distance(function(d) { return 150; })) // Set the desired distance between nodes
                .force("charge", d3.forceManyBody().strength(-200)) // Set a low repulsion force
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("x", d3.forceX(width / 2).strength(0.05))
                .force("y", d3.forceY(height / 2).strength(0.05));

            // Link Creation
            var link = svg.append("g")
                .attr("stroke", "#999")
                .attr("stroke-opacity", 0.6)
                .selectAll("line")
                .data(links)
                .enter().append("line")
                .attr("stroke-width", 1)  // Adjust stroke width as needed
                .attr("stroke", "#999");  // Remove arrowheads

            // Self-loop Creation
            var selfLoop = svg.append("g")
                .attr("fill", "none")
                .attr("stroke", "#999")
                .attr("stroke-opacity", 0.6)
                .selectAll("path")
                .data(selfLoops)
                .enter().append("path")
                .attr("class", "self-loop")
                .attr("d", function(d) { 
                  var node = nodes.find(node => node.id === d.source);
                  var r = 20; // Node radius
                  var x = node.x;
                  var y = node.y;
                  return "M " + (x + r) + "," + y + " A " + (r*1.5) + "," + (r*1.5) + " 0 1,0 " + (x - r) + "," + y; // Dynamically calculate the self-loop path
                });

            // Node Creation
            var node = svg.append("g")
                .attr("stroke", "#fff")
                .attr("stroke-width", 1.5)
              .selectAll("circle")
              .data(nodes)
              .enter().append("circle")
                .attr("r", 20)  // Adjust the radius of the circle to make it bigger
                .attr("fill", "#000")
                // Add drag behavior to nodes
                .call(d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended));

            // Text inside the Circle
            var text = svg.append("g").selectAll("text")
              .data(nodes)
              .enter().append("text")
                .text(function(d) { return d.name; })
                .attr("fill", "#fff")  // Set text color
                .attr("font-size", "12px")  // Set text font size
                .attr("text-anchor", "middle")  // Center the text horizontally
                .attr("dy", ".35em");  // Adjust vertical alignment of text

            // Tooltip Creation
            node.append("title")
                .text(d => d.name);

            // Simulation Event
            simulation.on("tick", () => {
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);

                selfLoop
                    .attr("d", function(d) { 
                      var node = nodes.find(node => node.id === d.source);
                      var r = 20; // Node radius
                      var x = node.x;
                      var y = node.y;
                      return "M " + (x + r) + "," + y + " A " + (r*1.5) + "," + (r*1.5) + " 0 1,0 " + (x - r) + "," + y; // Dynamically calculate the self-loop path
                    });

                node
                    .attr("cx", d => d.x)
                    .attr("cy", d => d.y);

                // Update text position with nodes
                text
                    .attr("x", function(d) { return d.x; })
                    .attr("y", function(d) { return d.y; });
            });

            // Drag functions
            function dragstarted(d) {
                if (!d3.event.active) simulation.alphaTarget(0.3).restart();
                d.fx = d.x;
                d.fy = d.y;
            }

            function dragged(d) {
                d.fx = d3.event.x;
                d.fy = d3.event.y;
            }

            function dragended(d) {
                if (!d3.event.active) simulation.alphaTarget(0);
                d.fx = null;
                d.fy = null;
            }
            """
        graph_string += "</script>"

        return graph_string