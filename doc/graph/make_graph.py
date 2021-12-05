import re


def make_sfdp_graph(file, output):
    all_checks = []
    regex = re.compile(r'{"filename": "(.*?)".*"uri": "(.*?)".*}')
    linkcheck_json = open(file, "r", encoding="utf-8")
    for line in linkcheck_json.readlines():
        all_checks.append(regex.sub('"\1" -> "\2";', line))
    linkcheck_json.close()

    output_graph = open(output, "w")
    for word in all_checks:
        output_graph.write(word)
    output_graph.close()



if __name__ == "__main__":
    json = "../build/linkcheck/output.json"
    make_sfdp_graph(json, "sfdp_graph.dot")

