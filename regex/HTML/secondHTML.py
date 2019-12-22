import re

document_input_string = '''
<div id="foo"><p id="a-p">stuff</p><p id="p2">other</p></div>
'''

content1 = {
    elemName: 'p',
    elemTags: 'id="a-p"',
    content: 'stuff'
}

content2 = {
    elemName: 'p',
    elemTags: 'id="p2"',
    content: 'other'
}

document = \
   { 
        elemName: 'div', 
        elemTags: 'id="foo"', 
        content: [content1, content2]
    }


htmlstr = '''
<div id="duff" class="doggy" 
style="yadda"><p>Duff got his hair did today</p>
<p id="pid">and I had to do some additional cuts</p>
</div>
<div id="second div" class="second class" style="second style">
'''

def search_for_tags():
    search_string = r'<(\w+)\s*(.*?)>'
    search_string_c = re.compile(search_string, re.DOTALL)
    return search_string_c.findall(htmlstr)

def search_for_attr(tag_content):
    """
    content string: something to be searched
    regex string: contains a regular expression
    tag_str_to_search: content
    """
    attr_re = r'(\w+)="(.*?)"\s*'
    attr_re_c = re.compile(attr_re, re.DOTALL)
    for attr_tuple in attr_re_c.findall(tag_content[1]):
        print(attr_tuple[0] + " - " + attr_tuple[1])
        # print(attr_tuple[1])

def main():
    for tag in search_for_tags():
        print(">>> " + tag[0] + " <<<")
        # print("---")
        search_for_attr(tag)
        # print("---")

main()