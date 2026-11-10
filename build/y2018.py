#!/usr/bin/env python3
"""2018年 大問Ⅰ (A)(B) 本文への登木式書き込み＋空所の手がかり。PDF化: node render.js y2018.html ../2018_I_annotated.pdf"""
import html
import pathlib
import re

from build import annotate_togi

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "y2018.html"
E = html.escape


def md(s):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", E(s))


# (段落, 文型, 注釈付き英文, 書き込みメモ, 和訳)  空所は【番号 答え】で表示
A = [
    ("第1段落", "If 節＋chances are (that) SV",
     "{M|<If {S'|someone} {V'i|【1 grew up】} {M'|<here in South Florida>}>}, {M|<chances are △>} {S|they} {Vt|had} {O|fruit trees} {M|<in their yard or in their neighborhood>}.",
     ["chances are (that) S V「たぶん〜だろう」→ 文頭の M 扱い（tactics 110 と同じ発想）。that の省略。",
      "★【1】主節が had（過去）＋後半の childhood home（言い換え）→「ここで育った人」grew up。grow up は完全自動詞なので後ろは M。"],
     "南フロリダで育った人なら、たぶん自分の家の庭か近所に果樹があっただろう。"),
    ("第1段落", "Maybe SV ①（Maybe の同形反復スタート）",
     "{M|Maybe} {M|<between games of basketball in a friend’s narrow alley driveway>} {S|they} {Vi|walked} {M|<down the lane>} {M|<to an abandoned lot (with a mango tree)>}.",
     ["【同形反復】Maybe S V が4回続く → 「育った人の思い出」の具体例の列挙。どれも同じ方向の内容。",
      "長い前＋名は全部 M（tactics 001）。骨格は they walked。"],
     "友人の家の狭い路地の車道でバスケットボールをする合間に、路地を歩いてマンゴーの木のある空き地まで行ったことがあるかもしれない。"),
    ("第1段落", "Maybe SVO with 〜 ②（語法）",
     "{M|Maybe} {S|their co-worker} {Vt|【2 bombarded】} {O|the office} {M|<every week>} {M|<with bags of softball-sized green avocados or pomelos>}.",
     ["★【2】【語法】空所の後ろが O（the office）＋with B → bombard A with B「A に B を浴びせる」。envelop は A in B、pitch・ventilate は with B を取らない。",
      "まず空所の後ろの「O＋前置詞」を見る → 動詞の語法で決まる。"],
     "同僚が毎週、ソフトボール大の緑のアボカドやザボンを袋に入れて職場にどっさり持ってきたかもしれない。"),
    ("第1段落", "Maybe SV [how SV] ③",
     "{M|Maybe} {S|they} {Vt|remember} {O|[how <every night at sunset>, {S'|escaped cockatoos} {V'|would pick} {M'|<at a neighbor’s papaya tree>}]}.",
     ["how のカタマリは remember の O（名詞のカタマリ：tactics 028）。how の直後に M（every night at sunset）が割り込んでいる。",
      "would は過去の習慣「よく〜したものだ」。escaped は過去分詞で cockatoos にかかる（tactics 013）。"],
     "毎晩日が沈むころ、逃げ出したオウムが近所のパパイヤの木をついばんでいたのを覚えているかもしれない。"),
    ("第1段落", "Maybe SV once 〜 and, 分詞, V O ( ) ④",
     "{M|Maybe} {S|they} {V|only learned to love} {O|lychees} {M|<once {S'|they} {V't|left} {O'|home} {M'|<for another city>} and, <{(V)|spotting} {(O)|the fruit} {(M)|<in a grocery in Chinatown>}>, {V't|bought} {O'|them} {M'|【3 impulsively】}, {M'|<only because they knew [△ that same fruit was hanging in the yard opposite their childhood home]>}>}.",
     ["once は従接「〜すると・〜してから」。once の中の V' は left と bought の2つを and が結ぶ（tactics 010・029）。間の spotting 〜 は分詞構文（tactics 052②）。",
      "★【3】only because「ただ〜という理由だけで」→ 深く考えず買った → impulsively（衝動的に）。",
      "【言い換え】their childhood home → 問1の「ここで育った」の裏づけ。"],
     "あるいは、別の町へ移るために家を出て初めてライチが好きになり、チャイナタウンの食料品店でその果物を見つけて、子どもの頃の家の向かいの庭に同じ果物がなっていたというだけの理由で、衝動的に買ったのかもしれない。"),
    ("第2段落", "分詞（否定）＋SVO",
     "{M|<Without taking a single class>}, {S|they} {Vt|knew} {O|[how to spot that fruit]}.",
     ["how to do は名詞のカタマリ（tactics 080）。Without taking a single class「授業を一度も受けずに」→ 問5 teacher’s を消す根拠。"],
     "授業を一度も受けなくても、彼らはその果物の見つけ方を知っていた。"),
    ("第2段落", "SVO（O が4つ並ぶ）",
     "{S|They} {Vt|knew} {O|[what it was], its other names, [when it was in 【4 season】], and [what it looked like <not only in a cardboard box in the grocery, but clustered heavy between the tree’s feathery leaves>]}.",
     ["【同形反復】knew の O が4つ：what 節／its other names／when 節／what 節。",
      "★【4】it＝その果物 → in season「旬で」。in place／in time／in turn も熟語だが果物に合わない。",
      "not only A but B：A＝in a cardboard box（店の箱の中）、B＝clustered heavy between leaves（木に実った姿）。"],
     "それが何なのか、別の名前、いつが旬なのか、そして食料品店の段ボール箱の中だけでなく、木の羽のような葉の間に重たげに房になっている姿まで知っていた。"),
    ("第2段落", "SVC＋同格（言い換え）",
     "{S|That} {V|is} {C|one of a 【5 native’s】 versions (of Miami)}, {C|one of their perspectives}.",
     ["★【5】【言い換え】後ろの one of their perspectives が同格。their＝ここで育った人 → native’s（地元育ちの人の）。",
      "teacher’s は without taking a single class と逆、traveler’s は native の反対。"],
     "それが、地元育ちの人にとってのマイアミの一つの姿、彼らの視点の一つである。"),
    ("第3段落", "SVO, and SV（with 〜 の同形反復）",
     "{S|We all} {Vt|experience} {O|the places (where we live)} {M|<in so many ways>}, and {S|these ways} {Vi|change} {M|<with the times of year, with our goals, our families, and our lives>}.",
     ["where は関係副詞（中は完全文：tactics 031）。【同形反復】with 〜 , with 〜 で変化の要因を並べる。",
      "★ the places where we live → 問6（local）の土台となるテーマ。"],
     "私たちはみな、住んでいる場所をさまざまな形で経験しており、その形は季節や、目標、家族、人生とともに変わっていく。"),
    ("第3段落", "命令文 ; 命令文 ; 命令文, and SV（命令文＋and）",
     "{V|Learn} {O|a piece of 【6 local】 history}; {V|know} {O|[who designed a building]}; {V|be able to identify} {O|a bird or a graffiti tag}, and {M|suddenly}, {S|you} {Vi|live} {M|<in a different place>}, and {S|that place} {Vi|will travel} {M|<with you>}.",
     ["【同形反復】セミコロンで命令文が3つ並ぶ（Learn ～ ; know ～ ; be able to ～）。命令文＋and S V「〜すれば S は V する」。",
      "★【6】3つの例（歴史・建物・鳥や落書き）に共通するのは「住んでいる場所の知識」→ local。colonial は狭すぎ、global は逆、natural は建物・落書きと合わない。"],
     "地元の歴史を少し学び、誰が建物を設計したかを知り、鳥やグラフィティのタグを見分けられるようになれば、突然あなたは別の場所に住んでいることになり、その場所はあなたとともに旅をするのだ。"),
    ("第3段落", "命令文, and SV",
     "{V|Spot} {O|ripe Spanish limes} {M|<as a child>}, and {S|you}{V|’ll} {M|still} {V|spot} {O|them} {M|today}.",
     ["命令文＋and の同じ型の繰り返し（前の文と同形反復）。「子どもの頃に〜を見つければ、今でも見つけられる」。"],
     "子どもの頃に熟したスパニッシュライムを見つけていれば、今でも見つけられるだろう。"),
    ("第3段落", "SV（現在完了の受身）",
     "{S|A layer (of the finite)} {V受|has been laid} {M|<【7 behind】 the infinite>}.",
     ["lay の受身 → be laid ＋場所の M。the finite（有限のもの＝具体的な知識）／the infinite（無限のもの＝漠然とした風景）。",
      "★【7】【言い換え】直後の文 It has always been there, but … something you didn’t even think about（ずっとそこにあったのに気づかなかった）→ 見えない「後ろ」に敷かれていた → behind。"],
     "無限なものの背後に、有限なものの層が敷かれているのだ。"),
    ("第3段落", "SVM, but SVC＋同格",
     "{S|It} {V|has} {M|always} {V|been} {M|there}, but {S|it} {V|was} {M|almost} {C|a blank space}, {C|something (△ you didn’t even think about ●)}.",
     ["it＝a layer of the finite。be there「そこにある」（存在の be：tactics 075②）。",
      "something △ you didn’t even think about ● は関係詞の省略（tactics 030）。a blank space の言い換え。→ 問7の根拠"],
     "それはずっとそこにあったのだが、ほとんど空白で、考えもしなかったものなのだ。"),
]

B = [
    ("第1段落", "SV受＋同格 that（ダッシュで言い換え）",
     "{S|Modern science and modern empires} {V受|were motivated} {M|<by the restless feeling [that perhaps {S'|something important} {V'i|awaited} {M'|<beyond the horizon>}] — something (△ they had better explore and master ●)>}.",
     ["the feeling that 〜 は同格の that（中は完全文：tactics 033②）。",
      "ダッシュ以下は something important の言い換え。something △ they had better explore and master ● は関係詞の省略（tactics 030）。"],
     "近代科学と近代帝国はどちらも、地平線の向こうに何か重要なものが待っているかもしれない、探検して支配したほうがよい何かが、という落ち着かない気持ちに突き動かされていた。"),
    ("第1段落", "SV（比較）",
     "Yet {S|the connection (between science and empire)} {Vi|went} {M|much deeper}.",
     ["Yet＝「だが」。much は比較級の強調（tactics 105）。→ 次の文で「より深い結びつき」を具体化する予告。"],
     "だが、科学と帝国の結びつきはそれよりはるかに深かった。"),
    ("第1段落", "Not just A, but also B ＋ V受（those の言い換え）",
     "{S|Not just the motivation, but also the 【8 practices】 (of empire-builders)} {V受|were entangled} {M|<with those (of scientists)>}.",
     ["【並列】Not just A but also B：A＝motivation（動機）と並ぶ B → 動機 ⇔ 実際の行い＝practices。",
      "★【8】those＝the practices（複数）→ 空所も複数形。次の段落の具体的な行動（地図作り・測量・蝶の分類）とも一致。"],
     "動機だけでなく、帝国建設者たちの実践もまた、科学者たちの実践と絡み合っていた。"),
    ("第1段落", "SVC, while SVC（たすき掛けの対比）",
     "{M|<For modern Europeans>}, {S|[building an empire]} {V|was} {C|a scientific project}, {M|<while {S'|[setting up a scientific discipline]} {V'|was} {C'|an 【9 imperial】 project}>}.",
     ["【対比・同形反復】while の前後が同じカタチ（動名詞 S＋was＋a 〜 project）。",
      "★【9】帝国 → 科学的、科学 → ？ のたすき掛け → imperial（帝国的な）。動名詞の S は tactics 041③。"],
     "近代ヨーロッパ人にとって、帝国を築くことは科学的な事業であり、一方で科学の学問分野を確立することは帝国的な事業だった。"),
    ("第2段落", "When 節＋SVO to do ×4（同形反復）",
     "{M|<When {S'|the Muslims} {V't|conquered} {O'|India}>}, {S|they} {V|did not bring} {M|【10 along】} {O|archaeologists (to systematically study Indian history), 【11 anthropologists】 (to study Indian cultures), geologists (to study Indian soils), or zoologists (to study Indian fauna)}.",
     ["★【10】bring along O「O を連れていく」（along は副詞なので O の前に置ける）。with は前置詞なので後ろに名詞が必要。",
      "★【11】【同形反復】「学者 to study 〜」が4つ：考古学者→歴史／（　）→文化／地質学者→土／動物学者→動物。文化を研究するのは anthropologists（anthropo＝人間）。",
      "to systematically study は分離不定詞（tactics 097）。"],
     "イスラム教徒がインドを征服したとき、彼らはインドの歴史を体系的に研究する考古学者も、インドの文化を研究する人類学者も、インドの土壌を研究する地質学者も、インドの動物相を研究する動物学者も連れていかなかった。"),
    ("第2段落", "When 節＋SVO（対比）",
     "{M|<When {S'|the British} {V't|conquered} {O'|India}>}, {S|they} {Vt|did} {O|all of these things}.",
     ["【対比・同形反復】前の文と同じ When S’ conquered India, 〜 の形で、ムスリム ⇔ イギリスを対比。"],
     "イギリス人がインドを征服したとき、彼らはそのすべてを行った。"),
    ("第2段落", "SV受 ／ SVO",
     "{M|<On 10 April 1802>} {S|the Great Survey of India} {V受|was launched}. {S|It} {Vt|lasted} {O|sixty years}.",
     ["launch「始める」。last は「続く」（後ろの sixty years は期間を表す語）。"],
     "1802年4月10日、インド大測量が開始された。それは60年続いた。"),
    ("第2段落", "SVO＋分詞構文 ×3（同形反復）",
     "{M|<With the help of tens of thousands of native labourers, scholars and guides>}, {S|the British} {M|carefully} {Vt|mapped} {O|the whole of India}, {M|<{(V)|marking} {(O)|borders}, {(V)|measuring} {(O)|distances}, and even {(V)|calculating} {(M)|<for the first time>} {(O)|the exact height (of Mount Everest and the other Himalayan peaks)}>}.",
     ["marking・measuring・calculating の3つの分詞を and でまとめる（同形反復：tactics 029）。分詞構文のミクロ S は the British（tactics 040）。",
      "calculating の O が長いので、M（for the first time）が V と O の間に入っている。"],
     "何万人もの現地の労働者、学者、案内人の助けを借りて、イギリス人はインド全土を丹念に地図にし、国境を記し、距離を測り、さらにはエベレストやほかのヒマラヤの峰々の正確な高さを初めて算出した。"),
    ("第2段落", "SVO, but SVO to do ×4（同形反復）",
     "{S|The British} {Vt|explored} {O|the military resources (of Indian provinces) and the location (of their gold mines)}, but {S|they} {M|also} {Vt|【12 took】} {O|the trouble} {M|<to collect information about rare Indian spiders, to catalogue colourful butterflies, to trace the ancient origins of 【13 extinct】 Indian languages, and to dig up forgotten ruins>}.",
     ["★【12】【語法】take the trouble to do「わざわざ〜する」。but also で「軍事・金鉱（役に立つもの）だけでなく、役に立たなそうなものまで」。",
      "【同形反復】to collect / to catalogue / to trace / to dig up の4つの to do。",
      "★【13】並んでいる dig up **forgotten** ruins と方向をそろえる → 失われた言語＝extinct（消滅した）。ancient origins とも合う。"],
     "イギリス人はインド各州の軍事資源や金鉱の場所を調べたが、それだけでなく、珍しいインドのクモの情報を集め、色とりどりの蝶を分類し、消滅したインドの言語の古い起源をたどり、忘れられた遺跡を掘り起こすことまでわざわざ行った。"),
    ("第3段落", "SVC＋非制限 which（V' ×2）",
     "{S|Mohenjo-daro} {V|was} {C|one of the chief cities (of the Indus Valley civilization)}, {M|(which ⟪S'欠⟫ {V'i|flourished} {M'|<in the third millennium BC>} and {V'受|was destroyed} {M'|<around 1900 BC>})}.",
     ["which の中は S 欠（tactics 031）。flourished と was destroyed を and が結ぶ。先行詞は the Indus Valley civilization。"],
     "モヘンジョダロはインダス文明の主要都市の一つで、この文明は紀元前3千年紀に栄え、紀元前1900年ごろに滅びた。"),
    ("第3段落", "SVOO（give O₁ a 〜 glance）＋ダッシュの挿入",
     "{S|None (of India’s pre-British rulers)} — neither the Mauryas, nor the Guptas, nor the Delhi sultans, nor the great Mughals — {V|had given} {O|the ruins} {O|a 【14 second】 glance}.",
     ["ダッシュ内は None の具体例（neither A nor B nor C …）。挿入なので飛ばして V（had given）につなぐ（tactics 036）。",
      "give O₁ O₂（tactics 022）。",
      "★【14】【対比】次の文の But … took notice（注目した）⇔ 誰も見向きもしなかった → not give 〜 a second glance「二度見もしない＝見向きもしない」。"],
     "イギリス以前のインドの支配者は誰ひとり――マウリヤ朝もグプタ朝もデリーのスルタンも偉大なムガル帝国も――その遺跡に見向きもしなかった。"),
    ("第3段落", "SVO ; SV受 and SV受",
     "But {S|a British archaeological survey} {Vt|took} {O|notice} {M|<of the site>} {M|<in 1922>}; {S|the site} {V受|was excavated} and {S|the first great civilization (of India)} {V受|was uncovered}.",
     ["take notice of 〜「〜に注目する」。But で前の文と対比 → 問14の根拠。"],
     "しかし、イギリスの考古学調査隊が1922年にその遺跡に注目し、遺跡は発掘され、インド最初の偉大な文明が掘り起こされたのである。"),
]

CLUES = [
    ("1", "grew up", "時制＋言い換え", "had（過去）＋ childhood home"),
    ("2", "bombarded", "語法", "( ) the office with B → bombard A with B"),
    ("3", "impulsively", "理由の M", "only because（ただ〜だけの理由で）"),
    ("4", "season", "熟語", "主語が果物 → in season"),
    ("5", "native’s", "言い換え（同格）", "one of their perspectives"),
    ("6", "local", "同形反復", "命令文 ; 命令文 ; 命令文 の共通点＝住む場所"),
    ("7", "behind", "直後の文の言い換え", "It has always been there, but … didn’t even think about"),
    ("8", "practices", "並列", "Not just the motivation, but also the ( ) … those"),
    ("9", "imperial", "対比（たすき掛け）", "empire → scientific, while science → ( )"),
    ("10", "along", "語法", "bring along O"),
    ("11", "anthropologists", "同形反復", "学者 to study 〜 ×4"),
    ("12", "took", "語法", "take the trouble to do"),
    ("13", "extinct", "並列", "forgotten ruins と方向をそろえる"),
    ("14", "second", "対比", "None … a ( ) glance ⇔ But … took notice"),
]

CSS_EXTRA = """
table.cl { width:100%; border-collapse:collapse; font-size:9.6pt; margin-bottom:3mm; }
.cl td, .cl th { border:1px solid #999; padding:1mm 2mm; vertical-align:top; }
.cl th { background:var(--soft); }
.cl td.n { width:9mm; text-align:center; font-weight:bold; }
.cl td.a { width:30mm; font-family:"Liberation Serif",serif; font-weight:bold; background:#fff1a6; }
.cl td.t { width:32mm; font-weight:bold; color:#b3261e; }
.notes li b { color:#b3261e; }
"""


def block(sents, start):
    out, prev = [], None
    for n, (para, pat, ann, notes, ja) in enumerate(sents, start):
        if para != prev:
            out.append(f'<h3 class="ph">{E(para)}</h3>')
            prev = para
        li = "".join(f"<li>{md(x).replace('★', '<b>★</b>')}</li>" for x in notes)
        out.append(f"""
<div class="sent">
  <div class="sn">{n}</div>
  <div class="pattern">{E(pat)}</div>
  <div class="en togi">{annotate_togi(ann)}</div>
  <ul class="notes">{li}</ul>
  <div class="ja"><span class="jt">訳</span>{E(ja)}</div>
</div>""")
    return "".join(out)


def build():
    for s in A + B:
        assert s[2].count("{") == s[2].count("}"), s[2]
    css = (HERE / "style.css").read_text() + CSS_EXTRA
    demo = annotate_togi("{S|S} {Vt|V} {O|O} {M|M}")
    clues = "".join(f'<tr><td class="n">{n}</td><td class="a">{E(a)}</td><td class="t">{E(t)}</td><td class="e">{E(c)}</td></tr>' for n, a, t, c in CLUES)
    body = f"""
<div class="cover">
  <div class="kicker">2018年 英語 大問Ⅰ　本文書き込み（登木式）</div>
  <h1>(A) マイアミの果物／(B) 科学と帝国</h1>
</div>
<div class="legend togi">
  <div>{demo}　黄色＝S・V・O・C、緑＝M。V の右下：i＝自動詞、t＝他動詞、受＝受身。従属節は S'・V'…、準動詞は (V)(O)(M)</div>
  <div>△＝省略　<span class="gap">●</span>＝欠けている位置　【番号 答え】＝空所と正解　★＝空所を決める手がかり</div>
  <div>【同形反復】【対比】【言い換え】【語法】【並列】＝本文に書き込む目印</div>
</div>
<h3>空所の手がかり一覧</h3>
<table class="cl"><tr><th>問</th><th>答え</th><th>手がかりの種類</th><th>本文のどこを見るか</th></tr>{clues}</table>
<section class="sec page"><h2><span class="num">A</span>マイアミの果物（Forager）</h2>{block(A, 1)}</section>
<section class="sec page"><h2><span class="num">B</span>科学と帝国（Sapiens）</h2>{block(B, 1)}</section>
"""
    OUT.write_text(f"""<!doctype html><html lang="ja"><head><meta charset="utf-8">
<title>2018年 大問Ⅰ 書き込み</title><style>{css}</style></head><body>{body}</body></html>""")
    print("wrote", OUT)


if __name__ == "__main__":
    build()
