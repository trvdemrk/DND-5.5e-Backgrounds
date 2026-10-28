from xml.etree.ElementTree import parse, Element

progressions_doc = parse('./patch8-bg3-files/Progressions.lsx')

ecount = 0
for ele in progressions_doc.iter():
    is_race_progression = False
    if ele.tag == 'node' and ele.get('id') == "Progression":
        has_level_one_attribute = False
        has_race_attribute = False
        for attr in ele.iter('attribute'):
            if attr.get('id') == 'Level' and int(attr.get('value')) == 1:
                has_level_one_attribute = True
            if attr.get('id') == 'ProgressionType' and int(attr.get('value')) == 2:
                has_race_attribute = True
            if has_race_attribute and has_level_one_attribute:
                is_race_progression = True
                break
        if is_race_progression:
            origin_feat_selector=Element('attribute', {'id' : "Selectors", 'type': "LSString", 'value':"SelectSkills(233793b3-838a-4d4e-9d68-1e0a1089aba5,2)"})
            ele.append(origin_feat_selector)

progressions_doc.write('../Source/Public/55EBackgrounds/Progressions/Progressions.lsx')