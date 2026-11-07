#!/usr/bin/env python3
"""「1 国際女性デー」精読→速読 解説 HTML を生成する。PDF化: node render.js womensday.html ../womens_day_reading.pdf"""
import html
import pathlib

from build import annotate_togi, plain

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "womensday.html"
E = html.escape

# 本文（段落ごとの文）
PARAS = [
    ["Rallies were held around the world Thursday to celebrate International Women’s Day and to demand an end to the exploitation, discrimination and violence that women face."],
    ["Hundreds of women stopped traffic outside city hall in Madrid in Spain’s first national women’s strike, in protest against wage gaps and gender violence.",
     "A recent study found Spanish women on average were paid nearly 13 percent less than their male colleagues. (…)"],
    ["In Seoul, women’s groups used the day to boost support for the American-born #MeToo movement against sexual assault in the workplace.",
     "The movement has spread across the Asian economic giant after a female prosecutor revealed in January that she had been assaulted by a colleague several years ago, leading to the downfall of numerous high-profile men, including a provincial governor who was a leading presidential contender before he was accused of raping his secretary. (…)"],
    ["In Myanmar, de facto leader Aung San Suu Kyi urged women to build peaceful democracies using their strength in politics, economics and social issues. (…)"],
    ["And in China, students at Tsinghua University used the occasion to make light of a proposed constitutional amendment to scrap term limits for the country’s president."],
]

# (文型, 注釈付き英文, 精読メモ, 和訳)
SENTS = [
    ("SV（受身：SVO → SV）",
     "{S|Rallies} {V受|were held} {M|<around the world>} {M|<Thursday>} {M|<to {(V)|celebrate} {(O)|International Women’s Day}>} and {M|<to {(V)|demand} {(O)|an end (to the exploitation, discrimination and violence (that {S'|women} {V't|face} ⟪O'欠⟫))}>}.",
     ["were held＝be＋p.p.＝受身。hold O「O を開催する」は SVO なので、受身にすると O が1個減って SV で完全文（tactics 018）。V はこの1個だけ（tactics 010）。",
      "Thursday は前置詞なしの名詞だが、時間を表す「副」のシゴト（副詞的目的格：tactics 003⑤）なので M。",
      "完全文が成立した後ろの to celebrate 〜 / to demand 〜 は M（tactics 025）。to do のカタマリの中はミクロ文型 (V)(O)（tactics 034）。2つの to do を and が並べている（等位接続詞：tactics 029）。意味は「〜するために」（目的）。",
      "an end to 〜 の to は後ろが名詞なので前置詞の to（tactics 074）。「〜を終わらせること」。",
      "that women face は関・名の that。内側は face の O が欠けた不完全文（tactics 031・033①）。先行詞は the exploitation, discrimination and violence の3つ全部。"],
     "木曜日、国際女性デーを祝い、そして女性が直面している搾取・差別・暴力をなくすよう求めるために、世界各地で集会が開かれた。"),
    ("SVO（第3文型）",
     "{S|Hundreds (of women)} {Vt|stopped} {O|traffic} {M|<outside city hall (in Madrid)>} {M|<in Spain’s first national women’s strike>}, {M|<in protest (against wage gaps and gender violence)>}.",
     ["hundreds of 名＝「何百もの名」。数量表現は of までをまとめて読み、中心は women（tactics 071）。",
      "stop は他動詞で traffic が O。SVO で完全文が成立したので、残りはすべて M（tactics 025・027「文末M」）。",
      "outside 〜 / in 〜 / in protest against 〜 はすべて前＋名＝M（tactics 001：緑色）。in protest against 〜「〜に抗議して」。"],
     "マドリードでは、スペイン初の全国規模の女性ストライキで、何百人もの女性が市庁舎の外で交通を止め、賃金格差とジェンダーに基づく暴力に抗議した。"),
    ("SVO（O が that 節）",
     "{S|A recent study} {Vt|found} {O|[△ {S'|Spanish women} {M'|<on average>} {V'受|were paid} {O'|nearly 13 percent less} {M'|<than their male colleagues>}]}.",
     ["V（found・were paid）が2個あるのに接続詞が見えない → どこかに △（省略された that）がある（V の数の法則：tactics 010）。",
      "think・know・find などの思考・認識の V の後ろの従接 that は省略できる（tactics 005①）。SV [that S'V'] の V は「思う・知る・表明する」の意味（tactics 024）→「調査で〜とわかった」。",
      "pay O₁ O₂「O₁ に O₂ を支払う」（tactics 022）を受身にすると O が1個残る（SVOO ⇒ S be p.p. O：tactics 018）。残った O' が nearly 13 percent less「13％近く少ない額」。",
      "on average「平均して」は S' と V' の間に割り込んだ M'。than 〜 は比較の相手。"],
     "最近の調査で、スペインの女性は平均して、男性の同僚よりも13％近く少ない給料しか支払われていないことがわかった。"),
    ("SVO（第3文型）＋目的の to do",
     "{M|<In Seoul>}, {S|women’s groups} {Vt|used} {O|the day} {M|<to {(V)|boost} {(O)|support (for the American-born #MeToo movement (against sexual assault (in the workplace)))}>}.",
     ["文頭 M → S → V → O（tactics 027 の頻出パターン「文頭M・SV のアイダ・文末」）。In Seoul は前＋名＝M。",
      "use A to do「A を使って〜する／〜するために A を利用する」。to boost 〜 は完全文の後ろなので M（目的）。中身は (V)(O)（tactics 034）。",
      "名詞の後ろに続く (for 〜)(against 〜)(in 〜) は、それぞれ直前の名詞にかかる形容詞のカタマリ（前＋名＝M：tactics 001）。support → movement → assault と順にかかっていく。",
      "the day は前の文の International Women’s Day の言い換え。"],
     "ソウルでは、女性団体がこの日を利用して、職場での性的暴行に反対するアメリカ発の #MeToo 運動への支持を高めようとした。"),
    ("SV（第1文型）＋分詞構文（結果）",
     "{S|The movement} {Vi|has spread} {M|<across the Asian economic giant>} {M|<after {S'|a female prosecutor} {V't|revealed} {M'|<in January>} {O'|[that {S''|she} {V''受|had been assaulted} {M''|<by a colleague>} {M''|<several years ago>}]}>}, {M|<{(V)|leading} {(M)|<to the downfall (of numerous high-profile men), including a provincial governor (who ⟪S'欠⟫ {V'|was} {C'|a leading presidential contender} {M'|<before {S''|he} {V''受|was accused} {M''|<of {(V)|raping} {(O)|his secretary}>}>})>}>}.",
     ["長い文こそ「わからない時はまず V から探せ」（tactics 036）。主節の V は has spread の1個だけ。spread は「S 自身が広がる」完全自動詞なので SV で完成し、残りは全部 M（tactics 008・025）。",
      "after の後ろに S'V'（a female prosecutor revealed）があるので、after は従属接続詞。after 〜 ago までが副詞のカタマリ（M）。",
      "revealed [that 〜]：V that 〜 は従接の that で内側は完全文（tactics 033②・070）。had been assaulted は過去完了の受身：明かした（1月）よりも前に暴行された、という時間のズレ（大過去）。",
      "カンマ＋leading 〜 は分詞のカタマリが M になったもの（分詞構文：tactics 052②）。ing のミクロ S は文全体の S（tactics 040）→「運動が広がり、その結果〜につながった」（文末の分詞構文は「結果」で訳すと自然）。lead to 〜「〜につながる」。",
      "the downfall of 〜 は「名詞 of 名詞」のデキゴト解釈：「多数の著名な男性が失脚すること」（tactics 112）。",
      "including 〜「〜を含めて」は前置詞扱い。who は関係代名詞で内側は S が欠けた不完全文（tactics 031）。was が V'、a leading presidential contender が C'（S'＝C'：tactics 019）。",
      "before 〜 の内側：accuse A of B「B のことで A を告発する」の受身 → A is accused of B。raping は前置詞 of の後ろの動名詞（ミクロ文型 (V)(O)：tactics 034）。"],
     "この運動は、1月に女性検察官が数年前に同僚から暴行を受けていたことを明かした後、このアジアの経済大国全体に広がり、多数の著名な男性の失脚につながった。その中には、秘書への性的暴行で告発されるまでは有力な大統領候補だった道知事も含まれている。"),
    ("SVOC（第5文型：urge O to do）",
     "{M|<In Myanmar>}, {S|de facto leader Aung San Suu Kyi} {Vt|urged} {O|women} {C|to {(V)|build} {(O)|peaceful democracies}} {M|<{(V)|using} {(O)|their strength} {(M)|<in politics, economics and social issues>}>}.",
     ["de facto leader と Aung San Suu Kyi は同格（名詞のシゴト⑦：tactics 003）。「事実上の指導者であるアウン・サン・スー・チー氏」。",
      "urge O to do「O に〜するよう促す」。O（women）と C（to build 〜）に主述関係がある「O に C させる」作為系の SVOC（tactics 062）。",
      "using 〜 は分詞のカタマリで M（tactics 052②）。their＝women なので、使うのは女性たち（build する人）。「自分たちの力を使って」。",
      "politics, economics and social issues は A, B and C の並列（tactics 029）。"],
     "ミャンマーでは、事実上の指導者であるアウン・サン・スー・チー氏が、政治・経済・社会問題における自らの力を生かして平和な民主主義を築くよう、女性たちに呼びかけた。"),
    ("SVO（第3文型）＋目的の to do",
     "{M|<And in China>}, {S|students (at Tsinghua University)} {Vt|used} {O|the occasion} {M|<to {(V)|make light of} {(O)|a proposed constitutional amendment (to scrap term limits (for the country’s president))}>}.",
     ["第4文と同じ use A to do の型。同じカタチの文を並べて各国の様子を紹介している。the occasion も International Women’s Day の言い換え。",
      "make light of 〜「〜を軽んじる・茶化す」は群動詞としてまとめて1つの V（他動詞）と考える（tactics 076）。",
      "proposed は前から名詞にかかる過去分詞（played③型：tactics 013）→「提案された」。名詞の前に a proposed constitutional と形容詞が3つ並び、中心の名詞は amendment（tactics 015）。",
      "amendment (to scrap 〜) の to do は直前の名詞にかかる形容詞のカタマリ：「〜を撤廃する（という）改正案」。the country’s president＝中国の国家主席。"],
     "そして中国では、清華大学の学生たちがこの機会を利用して、国家主席の任期制限を撤廃するという憲法改正案を茶化した。"),
]

# 速読：骨格（黄色だけ）と スラッシュ・チャンク
SKELETON = [
    ("Rallies were held", "集会が開かれた", "なぜ？ → to celebrate / to demand（目的）"),
    ("Hundreds of women stopped traffic", "何百人もの女性が交通を止めた", "どこで・なぜ？ → in Madrid / in protest against"),
    ("A study found [women were paid 13% less]", "調査で女性の給料は13％少ないとわかった", "→ Q1 の答え"),
    ("women’s groups used the day to boost support", "女性団体がこの日を利用して支持を高めた", "何への？ → #MeToo movement"),
    ("The movement has spread, leading to the downfall of men", "運動が広がり、男性の失脚につながった", "きっかけ → after 〜 revealed"),
    ("Suu Kyi urged women to build democracies", "スー・チー氏は女性に民主主義を築くよう促した", "方法 → using their strength"),
    ("students used the occasion to make light of an amendment", "学生がこの機会に改正案を茶化した", "何の改正？ → to scrap term limits"),
]

CHUNKS = [
    [("Rallies were held", "集会が開かれた"), ("around the world Thursday", "木曜日に世界中で"),
     ("to celebrate International Women’s Day", "国際女性デーを祝うために"),
     ("and to demand an end", "そして終わりを求めるために"),
     ("to the exploitation, discrimination and violence", "搾取・差別・暴力の"), ("that women face.", "女性が直面している")],
    [("Hundreds of women stopped traffic", "何百もの女性が交通を止めた"), ("outside city hall in Madrid", "マドリードの市庁舎の外で"),
     ("in Spain’s first national women’s strike,", "スペイン初の全国女性ストで"),
     ("in protest against wage gaps and gender violence.", "賃金格差とジェンダー暴力に抗議して")],
    [("A recent study found", "最近の調査でわかった"), ("△ Spanish women on average were paid", "（何が？）スペインの女性は平均して支払われていた"),
     ("nearly 13 percent less", "13％近く少なく"), ("than their male colleagues.", "男性の同僚より")],
    [("In Seoul,", "ソウルでは"), ("women’s groups used the day", "女性団体がその日を使った"),
     ("to boost support", "支持を高めるために"), ("for the American-born #MeToo movement", "アメリカ発の #MeToo 運動への"),
     ("against sexual assault in the workplace.", "職場での性的暴行に反対する")],
    [("The movement has spread", "その運動は広がった"), ("across the Asian economic giant", "そのアジアの経済大国中に"),
     ("after a female prosecutor revealed in January", "1月に女性検察官が明かした後"),
     ("that she had been assaulted by a colleague", "（何を？）同僚に暴行されていたことを"), ("several years ago,", "数年前に"),
     ("leading to the downfall", "（その結果）失脚につながった"), ("of numerous high-profile men,", "多数の著名な男性の"),
     ("including a provincial governor", "道知事も含めて"), ("who was a leading presidential contender", "（その人は）有力な大統領候補だった"),
     ("before he was accused", "彼が告発される前は"), ("of raping his secretary.", "秘書に性的暴行をしたことで")],
    [("In Myanmar,", "ミャンマーでは"), ("de facto leader Aung San Suu Kyi", "事実上の指導者スー・チー氏が"),
     ("urged women", "女性たちに促した"), ("to build peaceful democracies", "（何を？）平和な民主主義を築くよう"),
     ("using their strength", "自分たちの力を使って"), ("in politics, economics and social issues.", "政治・経済・社会問題における")],
    [("And in China,", "そして中国では"), ("students at Tsinghua University", "清華大学の学生たちが"),
     ("used the occasion", "その機会を使った"), ("to make light of", "茶化すために"),
     ("a proposed constitutional amendment", "提案された憲法改正案を"), ("to scrap term limits", "（どんな？）任期制限を撤廃する"),
     ("for the country’s president.", "その国の国家主席の")],
]

QUIZ = [
    ("Q1", "スペインではどのくらいの男女の賃金格差がある？",
     "女性の給料は、平均して男性の同僚より<b>13％近く低い</b>。",
     "第3文 Spanish women on average were paid nearly 13 percent less than their male colleagues. pay O₁ O₂ の受身で O が残った形（tactics 018・022）。nearly は「ほぼ・〜近く」（13％弱）。"),
    ("Q2", "下線部❶ a leading presidential contender はどのような意味？",
     "「<b>有力な大統領候補</b>（大統領選の最有力候補の一人）」。",
     "leading は名詞の前の形容詞「主要な・一流の」、presidential「大統領（選）の」、contender「競争者・候補者」。who 節の C'（S'＝C'）なので「その道知事＝有力な大統領候補だった」（tactics 019）。before 〜 があるので「告発されるまでは」有力候補だった、という含み。"),
    ("Q3", "下線部❷ a proposed constitutional amendment にはどのような内容が含まれている？",
     "<b>国家主席（the country’s president）の任期制限を撤廃する</b>という内容。",
     "直後の to scrap term limits for the country’s president が amendment にかかる形容詞のカタマリ（名詞＋to do）。scrap「廃止する」、term limits「任期制限」。"),
]

VOCAB = [
    ("rally", "集会"), ("exploitation", "搾取"), ("discrimination", "差別"), ("wage gap", "賃金格差"),
    ("boost", "〜を後押しする"), ("assault", "暴行（する）"), ("prosecutor", "検察官"),
    ("downfall", "失脚・没落"), ("high-profile", "注目を集める・著名な"), ("provincial governor", "（州・道の）知事"),
    ("contender", "競争者・候補者"), ("accuse A of B", "B のことで A を告発する"), ("de facto", "事実上の"),
    ("urge O to do", "O に〜するよう促す"), ("make light of", "〜を軽んじる・茶化す"), ("constitutional", "憲法の"),
    ("amendment", "修正案"), ("scrap", "〜を廃止する"), ("term limit", "任期制限"),
]

CSS_EXTRA = """
.lead { font-size:10pt; color:#333; margin:0 0 3mm; }
.fulltext p { margin:0 0 2.2mm; }
table.vocab { width:100%; border-collapse:collapse; font-size:9.5pt; margin-top:2mm; }
.vocab td { border-bottom:1px solid var(--rule); padding:.6mm 2mm; }
.vocab td.w { font-family:"Liberation Serif",serif; font-weight:bold; width:28%; }
.motto { border:2px solid var(--ink); padding:3mm 4mm; margin:0 0 4mm; font-size:10pt; line-height:1.8; }
.motto b { font-size:11pt; }
table.skel { width:100%; border-collapse:collapse; font-size:9.6pt; }
.skel td, .skel th { border:1px solid #999; padding:1mm 2mm; vertical-align:top; }
.skel th { background:var(--soft); }
.skel td.e { font-family:"Liberation Serif",serif; background:#fff1a6; width:38%; }
.skel td.n { text-align:center; width:7mm; }
.chunk { margin:0 0 3mm; break-inside:avoid; border-bottom:1px dashed var(--rule); padding-bottom:2mm; }
.chunk .c { display:inline-block; margin:0 1mm 1.2mm 0; vertical-align:top; }
.chunk .c .ce { font-family:"Liberation Serif",serif; font-size:11pt; }
.chunk .c .cj { display:block; font-size:8.3pt; color:#1d4ed8; line-height:1.3; }
.chunk .sl { color:#b3261e; font-weight:bold; margin:0 1mm; }
.flow .block { border:1.5px solid var(--ink); padding:2mm 4mm; break-inside:avoid; font-size:10pt; }
.flow .arrow { text-align:center; line-height:1.4; }
.points li { margin-bottom:1.2mm; }
"""


def build():
    # 注釈と本文の一致チェック
    flat = [s for p in PARAS for s in p]
    assert len(flat) == len(SENTS)
    for s, (_, ann, _, _) in zip(flat, SENTS):
        body = s.replace(" (…)", "")
        assert plain(ann).replace("△ ", "") == body, (plain(ann), body)

    css = (HERE / "style.css").read_text() + CSS_EXTRA
    parts = []

    # 表紙・本文
    lines = "".join(f"<p>{E(' '.join(p))}</p>" for p in PARAS)
    vocab = "".join(f'<tr><td class="w">{E(w)}</td><td>{E(j)}</td></tr>' for w, j in VOCAB)
    parts.append(f"""
<div class="cover">
  <div class="kicker">英文読解戦略プリントで読む　精読 → 速読</div>
  <h1>1 国際女性デー <small>International Women’s Day（190 words）</small></h1>
  <ol class="toc"><li>本文と語句</li><li>QUIZ 解答</li><li>精読：文構造と公式</li><li>速読：骨格読み・スラッシュリーディング</li><li>記事の流れ</li><li>全訳</li></ol>
</div>
<div class="motto"><b>精読の上に速読がある。</b>　まず1文ずつ S・V・O・C を確定し、「なぜそう読めるのか」を公式（tactics）で説明できる状態にする（第3章）。
それができたら、黄色（S・V・O・C）の骨格だけを拾い、緑（M）は「何の説明か」を予想しながら左から右へ流す（第4章）。速読は「読み飛ばし」ではなく、精読で身につけた判断を一瞬で行うことである。</div>
<h2><span class="num">1</span>本文と語句</h2>
<div class="fulltext">{lines}</div>
<table class="vocab">{vocab}</table>
""")

    # QUIZ
    qa = "".join(f"""
<div class="qa"><div class="qh">{q}　{E(t)}</div><p>▶ {a}</p><p class="qt">{E(why)}</p></div>""" for q, t, a, why in QUIZ)
    parts.append(f'<section class="sec page"><h2><span class="num">2</span>QUIZ 解答</h2>{qa}</section>')

    # 精読
    demo = annotate_togi("{S|S} {Vt|V} {O|O} {M|M}")
    blocks = []
    for n, (pattern, ann, notes, ja) in enumerate(SENTS, 1):
        li = "".join(f"<li>{E(x)}</li>" for x in notes)
        blocks.append(f"""
<div class="sent">
  <div class="sn">{n}</div>
  <div class="pattern">{E(pattern)}</div>
  <div class="en togi">{annotate_togi(ann)}</div>
  <ul class="notes">{li}</ul>
  <div class="ja"><span class="jt">訳</span>{E(ja)}</div>
</div>""")
    parts.append(f"""
<section class="sec page">
  <h2><span class="num">3</span>精読：文構造と公式</h2>
  <div class="legend togi">
    <div>{demo}　<b>主節</b>：黄色＝S・V・O・C（主役・中心・抽象）、緑色＝M（修飾語・具体・説明）（tactics 001・037）</div>
    <div>V の右下：<b>i</b>＝自動詞、<b>t</b>＝他動詞、<b>受</b>＝受身（be＋p.p.）　<b>従属節</b>：S'・V'・O'・C'・M'（さらに内側は S''…）</div>
    <div><span class="gap">●</span>＝関係詞の内側で名詞が欠けている位置　△＝省略された that　(V)(O)(M)＝準動詞のミクロ文型（tactics 034）</div>
    <div><span class="br">[ ]</span> 名詞のカタマリ　<span class="br">( )</span> 形容詞のカタマリ　<span class="br">&lt; &gt;</span> 副詞のカタマリ</div>
  </div>
  {''.join(blocks)}
</section>""")

    # 速読
    rows = "".join(f'<tr><td class="n">{i}</td><td class="e">{E(e)}</td><td>{E(j)}</td><td>{E(q)}</td></tr>'
                   for i, (e, j, q) in enumerate(SKELETON, 1))
    ch = []
    for i, cs in enumerate(CHUNKS, 1):
        inner = '<span class="sl">/</span>'.join(
            f'<span class="c"><span class="ce">{E(e)}</span><span class="cj">{E(j)}</span></span>' for e, j in cs)
        ch.append(f'<div class="chunk"><b>{i}</b>　{inner}</div>')
    parts.append(f"""
<section class="sec page">
  <h2><span class="num">4</span>速読：骨格読み・スラッシュリーディング</h2>
  <h3>① 骨格読み ― 黄色（S・V・O・C）だけを拾う</h3>
  <p class="lead">第3章で緑（M）にした部分をいったん外すと、7文の「言いたいこと」はこれだけになる。右列は「その M が何を説明しに来るか」の予想。速読ではこの予想を持ちながら M を読む。</p>
  <table class="skel"><tr><th>#</th><th>骨格（S V O C）</th><th>意味</th><th>M で答えが来る問い</th></tr>{rows}</table>
  <h3>② スラッシュリーディング ― 英語の語順のまま意味をとる</h3>
  <p class="lead">カタマリ（tactics 020）の切れ目でスラッシュを入れ、前から順に意味をつなぐ。後ろから訳し上げずに「（何を？）」「（どんな？）」と疑問を立てて次のカタマリで答えを受け取るのがコツ。</p>
  {''.join(ch)}
  <h3>③ 速読で使う判断（精読で身につけたものの高速版）</h3>
  <ul class="points">
    <li><b>文頭の前＋名は M</b>（In Seoul, / In Myanmar, / And in China,）。ニュース記事ではここが「次の話題（場所）」の目印になる。</li>
    <li><b>まず V を探す</b>（tactics 036）。第5文のような長文でも、主節の V は has spread の1個。V が見つかれば S の範囲と文型が決まり、残りは M として流せる。</li>
    <li><b>V が2個で接続詞が見えなければ △ を補う</b>（tactics 010・005）。第3文 found △ women were paid。</li>
    <li><b>完全文の後ろの to do・ing は M</b>（tactics 025）。to do なら「〜するために」、カンマ＋ing なら「そして〜」と前から訳し下ろす。</li>
    <li><b>言い換えを追う</b>：International Women’s Day → the day → the occasion、Seoul（韓国）→ the Asian economic giant、#MeToo movement → The movement。同じものを別の語で言っていると気づけば、知らない表現でも推測できる。</li>
  </ul>
</section>""")

    # 記事の流れ
    parts.append("""
<section class="sec page">
  <h2><span class="num">5</span>記事の流れ（パラグラフ構成）</h2>
  <div class="flow">
    <div class="block"><b>第1段落（リード）</b>　世界各地で国際女性デーの集会 ― 目的：①祝う ②搾取・差別・暴力の終結を求める<br><span style="color:#555">ニュース記事は最初の1文に「いつ・どこで・何が・なぜ」をまとめる。ここを精読すれば全体の予想がつく。</span></div>
    <div class="arrow">▼ 具体例（国別）</div>
    <div class="block"><b>第2段落　スペイン（マドリード）</b>　初の全国女性スト／賃金格差への抗議 ― 根拠：女性の賃金は約13％低い</div>
    <div class="arrow">▼</div>
    <div class="block"><b>第3段落　韓国（ソウル）</b>　#MeToo 運動への支持 ― 経緯：女性検察官の告発 → 運動の拡大 → 有力者の失脚（大統領候補だった知事も）</div>
    <div class="arrow">▼</div>
    <div class="block"><b>第4段落　ミャンマー</b>　スー・チー氏が女性に平和な民主主義づくりを呼びかけ</div>
    <div class="arrow">▼</div>
    <div class="block"><b>第5段落　中国</b>　清華大学の学生が国家主席の任期制限撤廃案を茶化す</div>
  </div>
  <p class="lead" style="margin-top:4mm">第2段落以降は「In ＋場所, S V 〜」という同じカタチの繰り返し（一般論 → 具体例の列挙）。一度この型をつかめば、各段落は「場所」「誰が」「何をしたか」の3点を拾うだけで速く正確に読める。</p>
</section>""")

    # 全訳
    tr = "".join(f"<p>{E(''.join(SENTS[i][3] for i in idx))}</p>"
                 for idx in ([0], [1, 2], [3, 4], [5], [6]))
    parts.append(f'<section class="sec page"><h2><span class="num">6</span>全訳</h2><div class="translation">{tr}</div></section>')

    OUT.write_text(f"""<!doctype html><html lang="ja"><head><meta charset="utf-8">
<title>1 国際女性デー 精読→速読</title><style>{css}</style></head><body>{''.join(parts)}</body></html>""")
    print("wrote", OUT)


if __name__ == "__main__":
    build()
