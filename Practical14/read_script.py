import xml.dom.minidom as minidom
import xml.sax
from datetime import datetime
import os

os.chdir("Practical14")

# input the xml file
XML_FILE = "go_obo.xml"

# initiate three dictionary
ontologies = ["molecular_function", "biological_process", "cellular_component"]

# --- analyze with DOM ---
def parse_with_dom():
    start_time = datetime.now()
    
    # decode XML file
    dom = minidom.parse(XML_FILE)
    terms = dom.getElementsByTagName("term")
    
    # statistic outcome
    is_a_counts = {ont: 0 for ont in ontologies}
    max_is_a_terms = {ont: ("", 0) for ont in ontologies}  # (term_name, is_a_count)
    
    for term in terms:
        namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue
        if namespace in ontologies:
            name = term.getElementsByTagName("name")[0].firstChild.nodeValue
            is_a_elements = term.getElementsByTagName("is_a")
            is_a_count = len(is_a_elements)
            
            # count the appearance number
            is_a_counts[namespace] += is_a_count
            
            # add the max is_a term
            current_max_name, current_max_count = max_is_a_terms[namespace]
            if is_a_count > current_max_count:
                max_is_a_terms[namespace] = (name, is_a_count)
    
    end_time = datetime.now()
    dom_time = (end_time - start_time).total_seconds()
    
    return is_a_counts, max_is_a_terms, dom_time

# --- analyze with SAX ---
class GOTermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self._current_tag = ""
        self._namespace = ""
        self._name = ""
        self._is_a_count = 0
        self._is_a_counts = {ont: 0 for ont in ontologies}
        self._max_is_a_terms = {ont: ("", 0) for ont in ontologies}
    
    def startElement(self, tag, attributes):
        self._current_tag = tag
        if tag == "term":
            self._namespace = ""
            self._name = ""
            self._is_a_count = 0
        elif tag == "is_a":
            self._is_a_count += 1
    
    def endElement(self, tag):
        if tag == "term":
            if self._namespace in ontologies:
                self._is_a_counts[self._namespace] += self._is_a_count
                current_max_name, current_max_count = self._max_is_a_terms[self._namespace]
                if self._is_a_count > current_max_count:
                    self._max_is_a_terms[self._namespace] = (self._name, self._is_a_count)
        self._current_tag = ""
    
    def characters(self, content):
        if self._current_tag == "namespace":
            self._namespace += content
        elif self._current_tag == "name":
            self._name += content

def parse_with_sax():
    start_time = datetime.now()
    
    # creat SAX decoder
    handler = GOTermHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(XML_FILE)
    
    end_time = datetime.now()
    sax_time = (end_time - start_time).total_seconds()
    
    return handler._is_a_counts, handler._max_is_a_terms, sax_time

# --- main programme ---
def main():
    # analyze with DOM
    dom_is_a_counts, dom_max_terms, dom_time = parse_with_dom()
    print("DOM Results:")
    for ont in ontologies:
        print(f"{ont}: {dom_is_a_counts[ont]} <is_a> elements, term with most <is_a>: {dom_max_terms[ont][0]} ({dom_max_terms[ont][1]} <is_a>)")
    print(f"DOM Time: {dom_time} seconds\n")
    
    # analyze with SAX
    sax_is_a_counts, sax_max_terms, sax_time = parse_with_sax()
    print("SAX Results:")
    for ont in ontologies:
        print(f"{ont}: {sax_is_a_counts[ont]} <is_a> elements, term with most <is_a>: {sax_max_terms[ont][0]} ({sax_max_terms[ont][1]} <is_a>)")
    print(f"SAX Time: {sax_time} seconds\n")
    
    # compare the time
    if dom_time < sax_time:
        print(f"# DOM was faster by {sax_time - dom_time} seconds")
    else:
        print(f"# SAX was faster by {dom_time - sax_time} seconds")

if __name__ == "__main__":
    main()