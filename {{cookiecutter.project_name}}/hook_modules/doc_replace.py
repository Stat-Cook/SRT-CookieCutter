import docx
import os


def read_doc(file_name: str, file_path: str = "."):
    is_doc = file_name.endswith("doc") or file_name.endswith("docx")

    if is_doc:
        path = os.path.join(file_path, file_name)
        return docx.Document(path)

    return False


class DocReplacer:

    def __init__(self, root):
        self.root: str = root
        self.replacement_dict: dict = dict()

        {% for key, value in cookiecutter.items() %}
        self.replacement_dict['[[{{key}}]]'] = '{{value | replace('\\', '\\\\')}}'
        {% endfor %}
        self.replacement_dict['[[Now]]'] = "2022/09/16"

    @property
    def walk(self):
        return os.walk(self.root)

    def replace_doc(self, doc: docx.Document):
        for paragraph in doc.paragraphs:
            for key, value in self.replacement_dict.items():
                paragraph.text = paragraph.text.replace(key, value)

        return doc

    def __call__(self):
        for root, folders, files in self.walk:
            for file in files:
                doc = read_doc(file, root)
                if doc:
                    doc = self.replace_doc(doc)
                    doc.save(os.path.join(root, file))
