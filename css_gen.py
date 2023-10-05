import os

def phrase_config_from_string(phrase_annotation):
    index = 0
    phrase_configuration = []
    while index < len(phrase_annotation):
        label = phrase_annotation[index]
        index += 1
        n_bars = ''
        while index < len(phrase_annotation) and phrase_annotation[index].isdigit():
            n_bars += phrase_annotation[index]
            index += 1
        phrase_configuration.append((label, int(n_bars)))
    return phrase_configuration

def colorize(figname, ph_anno):
    phs = phrase_config_from_string(ph_anno)
    str = f"\n#{figname} midi-visualizer .piano-roll-visualizer svg {{\n"
    str += "    background: linear-gradient(90deg, $l 1px, $t 1px 20px, #aaaaaa55 21px, $t 21px 40px, #aaaaaa55 41px, $t 41px 60px, #aaaaaa55 61px, $t 61px) left/80px repeat"
    cur = 0
    str += ", linear-gradient(90deg"
    for typ, len in phs:
        str += f", ${typ} {cur*80+1}px {(cur+len)*80-1}px, $l {(cur+len)*80-1}px {(cur+len)*80+1}px"
        cur += len
    str += ");\n}\n"
    return str


if __name__ == "__main__":
    fig2_mel_acc = colorize("fig2_melacc", "i4A4A4B8b4A4A8o4")
    fig2_cp = colorize("fig2_cp", "i4A4A4B8b4A4A8o4")
    with open("./styles.scss", "a") as f:
        f.write(fig2_mel_acc + fig2_cp)
