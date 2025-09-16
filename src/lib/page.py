import os
import re

from lib.html_markdown import markdown_to_html_node


def extract_title(markdown):
    title = re.search(r"^\s*# (.+)$", markdown, re.MULTILINE)
    if title is None:
        raise Exception("missing title")
    return title[1].strip()


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, encoding="utf-8") as f:
        with open(template_path, encoding="utf-8") as g:
            content = f.read()
            template = g.read()
            html_node = markdown_to_html_node(content)
            html = html_node.to_html()
            title = extract_title(content)

            # Replace placeholders in the template
            full_html = template.replace("{{ Title }}", title)
            full_html = full_html.replace("{{ Content }}", html)

            # Create directories if they don't exist yet
            dest_dir, _ = os.path.split(dest_path)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            # Save the output
            with open(dest_path, "w", encoding="utf-8") as output:
                output.write(full_html)

    print("Done!")
