from jinja2 import Template, Environment, FileSystemLoader
from pathlib import Path
from uuid import uuid4
from 
class BlockVisualizer:


    def visualizeGraph(self):
        env = Environment(loader=FileSystemLoader('templates/block_visualizer'))

        visualizer_template = env.get_template('templates/block_visualizer/block.jinja')
        output_from_parsed_template = visualizer_template.render()
        
        return output_from_parsed_template
    



def main():
    p = Path(__file__).parent/"templates" # sample relative path
    print(p)

    templateLoader = FileSystemLoader(searchpath=p)
    templateEnv = Environment(loader=templateLoader)
    TEMPLATE_FILE = "block.jinja"

    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(graph_nodes=graph.vertices, graph_edges=graph.edges)

    print(outputText)

    return outputText

if __name__ == "__main__":
    main()