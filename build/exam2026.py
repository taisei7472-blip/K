#!/usr/bin/env python3
"""2026年度 英語（大問Ⅰ〜Ⅲ）登木式 精読・設問解説 HTML。PDF化: node render.js exam2026.html ../exam2026_explained.pdf"""
import html
import pathlib
import re

from build import annotate_togi

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "exam2026.html"


def md(s):
    """**太字** だけ許す簡易変換。"""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(s))


# ===========================================================================
# 大問Ⅰ
# ===========================================================================
P1 = dict(
    title="大問Ⅰ　American English は英語を壊しているのか",
    flow=[
        ("[1]〜[3]", "問題提起", "イギリス人は昔からアメリカ英語を「野蛮・堕落」と非難してきた（1735年の Moore も、1995年のチャールズ皇太子も同じ）。"),
        ("[4]〜[6]", "皮肉・批判", "「野蛮」とは「自分と同じ話し方をしない」というだけのこと。英国には「新しいもの＝アメリカのもの＝悪い」という思い込みがある。"),
        ("[7]〜[11]", "筆者の主張", "言語の変化は避けられない。絶対的な権威はない。変わらない言語は死んだ言語である。"),
        ("[12]〜[13]", "根拠", "英米の違いは、アメリカがイギリス英語を崩したせいではない。両者が共通の祖先から別々に進化した結果である。"),
        ("[14]〜[15]", "結論", "Adams の予言どおり英語は世界に広がった。「変化＝破滅」と考える人にとってだけ、アメリカは英語を壊している。"),
    ],
    sents=[
        ("[2]", "SVOC の受身（S be p.p. C）",
         "{M|<In 1995>}, {M|<in much the same vein (as the comment 260 years earlier)>}, {S|His Royal Highness the Prince of Wales} {V受|was reported} {M|<by The Times>} {C|as {(V)|complaining} {(M)|<to a British Council audience>} {(O)|[that {S'|American English} {V'|is} {C'|‘very corrupting’}]}}.",
         ["report A as doing「A が〜していると報じる」は SVOC。受身にすると C（as complaining 〜）が残る（tactics 018：SVOC ⇒ S be p.p. C）。",
          "complain that 〜 の that は従接で、内側は完全文（tactics 033②）。",
          "【推測】vein を知らなくても、same 〜 as the comment 260 years earlier（1735＋260＝1995）から「[1] の Moore の発言と同じ調子・趣旨で」とわかる。→ 問3"],
         "1995年、260年前の発言とほぼ同じ調子で、チャールズ皇太子がブリティッシュ・カウンシルの聴衆に「アメリカ英語はひどく堕落を招く」と不満を述べたと『タイムズ』紙が報じた。"),
        ("[2]", "SV（受身）＋仮定法過去完了",
         "{M|<By this time>} {S|the barbarous use (of bluff) (for a steep bank)} {V受|had been civilized} {M|<by {(V受)|being adopted} {(M)|<into the usage (of the motherland)>}>}, but {M|doubtless} {M|<if {S'|the Prince} {V'i|had lived} {M'|about nine generations earlier}>}, {S|he} {Vt|would have agreed} {M|<with Francis Moore>} {O|[that {S'|bluff} {V'|is} {C'|a word (that ⟪S''欠⟫ {V''|shouldn’t be})}]}.",
         ["骨格は barbarous（野蛮な）⇔ civilized（文明化された）の対比。「野蛮な使い方」が「まともな語」になった、という流れ。",
          "being adopted は前置詞 by の後ろの動名詞（受身）。ミクロ文型は (V受)(M)（tactics 034）。",
          "motherland＝アメリカから見た「母国」＝イギリス。→ 問2",
          "if S' had p.p., S would have p.p. は仮定法過去完了。agree with A that 〜「〜という点で A に同意する」。"],
         "この頃までには、急な土手を指す bluff という野蛮な使い方も、母国の語法に取り入れられて洗練されていた。だが、皇太子が9世代ほど前に生きていたら、bluff は存在すべきでない語だという点で、きっと Moore に同意していただろう。"),
        ("[4]", "SVO ; SVO（関係詞 who の中に V' が2つ）",
         "{S|We} {Vt|owe} {O|the term barbarous} {M|<to the Greeks>}; {S|they} {Vt|pitied} {O|the poor foreigner (who ⟪S'欠⟫ {V'|could only stammer} {O'|‘bar-bar’} and {M'|hence} {V'|was} {C'|a ‘barbaros’})}.",
         ["owe A to B「A は B のおかげだ（A の由来は B）」。",
          "who の中は S が欠けた不完全文（tactics 031）。could only stammer と was の2つの V' を and が結んでいる（tactics 010・029）。"],
         "barbarous という語はギリシャ人に由来する。彼らは「バルバル」としか口ごもれず、それゆえ「バルバロス」である哀れな外国人を気の毒がったのだ。"),
        ("[4]", "SVC（S＝C）",
         "{S|Barbarians} {V|are} {M|simply} {C|those (who ⟪S'欠⟫ {V'i|do not talk} {M'|<as we do>})}, {M|<whether {S'|they} {V'|are} {C'|outsiders, Yanks or fellow countrymen and countrywomen (whose style we do not admire)}>}.",
         ["S＝C（tactics 019）。simply は「単に〜にすぎない」。「野蛮人＝自分と同じ話し方をしない人にすぎない」→ 純粋主義者を冷ややかに見る、筆者の皮肉なトーン（問4）。",
          "whether 〜 は「〜であろうと」の副詞のカタマリ（M）。whose style は admire の O が前に出たもの。"],
         "野蛮人とは、自分たちと同じ話し方をしない人にすぎない。それが外国人だろうと、ヤンキーだろうと、話し方の気に入らない同国人だろうと。"),
        ("[5]", "SVC＋関係詞 who（see A as B）",
         "{S|The journalist Edwin Newman} {V|is} {C|a linguistic prophet (who ⟪S'欠⟫ {V't|sees} {O'|the language style (of his fellow Americans)} {M'|as deadly})}.",
         ["The journalist と Edwin Newman は同格（名詞のシゴト⑦：tactics 003）。",
          "see A as B「A を B とみなす」。who の中は S 欠（tactics 031）。",
          "his fellow Americans の fellow は「仲間の・同じ立場の」→「彼と同じアメリカ人」。Newman はアメリカ人。→ 問5"],
         "ジャーナリストのエドウィン・ニューマンは、同胞のアメリカ人の言葉づかいを致命的だとみなす言語の予言者である。"),
        ("[6]", "SV and V受（分詞構文＝理由）",
         "{S|A knowledgeable British author} {Vi|complained} {M|<about the supposedly American pronunciation conTROVersy>} and {V受|was surprised} {M|<to hear [that {S'|the antepenult accent} {V'|is} {C'|unknown} {M'|<in the States>}, {M'|<being a recent British innovation>}]>}.",
         ["complained と was surprised の2つの V を and が結ぶ（tactics 010・029）。to hear は感情の原因の to do（M）。",
          "being 〜 は分詞のカタマリが M になったもの（分詞構文：tactics 052②）。ミクロ S は the accent（tactics 040）→「最近のイギリスの新しい発音なので」と理由を表す。→ 問8"],
         "ある博識なイギリス人作家は、アメリカ風とされる conTROVersy という発音に不満を述べたが、第3音節前のアクセントは最近のイギリスの新しい発音なのでアメリカでは知られていないと聞いて驚いた。"),
        ("[7]", "There＋V＋S（no の同形反復）＋though",
         "There {Vi|are} {S|no objective criteria (for judging worth in language), no linguistic Tables of the Law, no archetypical authority (called ‘The Dictionary’)}, {M|<though there {V'i|are} {S'|wannabe authoritarians} {M'|aplenty}>}.",
         ["no 〜 が3回くり返される同形反復で、「絶対的な権威は存在しない」ことを強調している。",
          "though は従接なので前後が対比になる。「権威はない。けれども権威者になりたがる人はたくさんいる」。",
          "【推測】wannabe＝want to be（〜になりたがる人）、authoritarian＝authority（権威）＋-ian（人）、aplenty＝plenty（たくさん）。→ 問6"],
         "言語の価値を判断する客観的基準も、言語の十戒も、『辞書』と呼ばれる原型的権威も存在しない。もっとも、権威者気取りの人はたくさんいるのだが。"),
        ("[8]", "SVC（S＝C）",
         "But {S|a language or anything else (that ⟪S'欠⟫ {V'i|does not change})} {V|is} {C|dead}.",
         ["S＝C（tactics 019）。「変化しないもの＝死んでいる」。裏返すと「変化する＝生きている」。→ 問7",
          "that は関・名の that で、中は S が欠けている（tactics 033①）。"],
         "だが、変化しない言語は、いや言語に限らず変化しないものはすべて、死んでいるのだ。"),
        ("[9]", "長い S（同格 that）＋ V＋C → 言い換え",
         "{S|The eighteenth-century hope [that {S'|a language} {V'受|could be ‘fixed’} — that is, improved, or changed <in a way (△ {S''|some self-appointed linguistic judge} {V''t|would approve of} ⟪O''欠⟫)> <until it reached a state of perfection> and then preserved <so that it would not thereafter degenerate or change in a way (△ the judge disliked ●)>]} — {V|was} {C|a chimera}. {S|It} {V|was} {C|an illusion (based on misunderstandings about the nature of language, values and human nature)}.",
         ["S がとても長いので、まず V を探す（tactics 036）。主節の V は was。",
          "hope [that 〜] は同格の that で、内側は完全文（tactics 033②）。",
          "a way △ some … judge would approve of ● は「名詞＋SV」で、関係詞の省略（tactics 030）。approve of の O が欠けている。",
          "【推測】chimera を知らなくても、次の文 It was an illusion で言い換えられている → chimera＝幻想。→ 問9"],
         "言語は「固定」できる、つまり自称言語審判が認める形で完成の域に達するまで改良・変更され、その後は審判の嫌うように劣化・変化しないよう保存できる、という18世紀の希望は、幻想にすぎなかった。それは、言語と価値と人間性の本質を誤解したことから生まれた幻想だった。"),
        ("[10]", "SV（change from A to B）",
         "{M|<During the recorded history of English>}, {S|the language} {Vi|has changed} {M|<from something quite incomprehensible (to a present-day English speaker), (which {S'|we} {V't|call} ⟪O'欠⟫ {C'|Old English})>} … {M|<to something equally incomprehensible (to many of us)>}, computerspeak ….",
         ["change from A to B「A から B へ変化する」。A＝古英語、B＝コンピュータ言葉。",
          "which の中は call O C の O が欠けた不完全文（tactics 031）。computerspeak は something と同格。",
          "has changed は現在完了 → 変化は今も続いている。→ 問11"],
         "記録に残る英語の歴史の中で、英語は、現代の話者にはまったく理解できない古英語と呼ばれるものから、私たちの多くにとって同じくらい理解できないもの、つまりコンピュータ言葉へと変化してきた。"),
        ("[13]", "not 〜. Rather …（否定 → 肯定）",
         "{S|The differences (between American and British)} {V|are not} {C|<due to [{(S)|Americans} {(V)|changing} {(M)|<from a British standard>}]>}. {S|American} {V|[ A ]} {C|corrupt British [ B ] barbarisms}. {M|Rather}, {S|both American and British} {Vi|evolved} {M|<in different ways>} {M|<from a common sixteenth-century ancestral standard>}.",
         ["Americans changing は「名詞＋ing」で、名詞を意味上の S として読む（tactics 032②）→「アメリカ人が変えたこと」。",
          "not 〜 . Rather …「〜ではない。むしろ…だ」。前の文が否定なので、空所の文も否定（is not）で続く。→ 問12"],
         "英米の違いは、アメリカ人がイギリスの標準から変えたことによるのではない。アメリカ英語は、崩れたイギリス英語に野蛮な語を足したもの、ではないのだ。むしろ英米の英語はともに、16世紀の共通の祖先から別々の形で進化したのである。"),
        ("[14]", "SVC＋because 節（S' の後ろに分詞の挿入）",
         "{S|The reason (of this)} {V|is} {C|obvious}, {M|<because {S'|the increasing population (in America), and their universal connection and correspondence (with all nations)} {V'|will}, {M'|<aided by the influence of England in the world, whether great or small>}, {V'|force} {O'|their language} {M'|<into general use>}>}.",
         ["because の中の V' は will … force。間に aided by 〜（過去分詞の M'）が割り込んでいる（tactics 027「S V のアイダの M」）。",
          "アメリカの人口増加は、英語を世界に広げる「プラスの要因」として描かれている。→ 問13"],
         "その理由は明らかだ。アメリカの人口増加と、あらゆる国とのつながりや交流が、イギリスの世界的影響力の大小にかかわらずその助けを得て、彼らの言語を一般的に使われるものにするからだ。"),
    ],
    qs=[
        ("1", "筆者の意見", "c", ["[7] Change in language is inevitable と [8] no one is required to like any changes を合わせると c。",
                                 "a は「どんな変化も歓迎すべき」が [8] と矛盾。b は [9] で chimera と否定された考え。d は [11] と逆（交流しないと違いが増える）。"]),
        ("2", "bluff について正しいもの", "c", ["根拠は [2] had been civilized by being **adopted** into the usage of the **motherland**。",
                                          "【推測】adopted＝選択肢の accepted。motherland＝アメリカ人の母国＝イギリス。barbarous ⇔ civilized の対比から「野蛮な語がまともな語として受け入れられた」とわかる。",
                                          "b「元の意味を失った」は書かれていない（意味は a steep bank のまま）。"]),
        ("3", "皇太子の発言に言及する意図", "c", ["in much the same vein as the comment 260 years earlier。1735年と1995年で同じ批判がある → 批判は現代まで続いている。"]),
        ("4", "[4] のトーン", "b（ironic and sceptical）",
         ["One way Americans are ruining English is by changing it は字面どおりではない。筆者は [7] で変化は避けられないと言っているので、「変えたら壊したことになるの？」という皮肉。",
          "Barbarians are **simply** those who do not talk as we do の simply（〜にすぎない）にも注目。「野蛮」というレッテルは身内びいきにすぎない、と冷ややかに見ている。",
          "a・c・d は純粋主義者側の態度。"]),
        ("5", "[5] について NOT true", "a", ["**※ 間違えた問題。** [5] his **fellow** Americans から、Newman はアメリカ人。a の「イギリス人」が誤り。",
                                          "b：verbosity（冗長）・euphemism（婉曲）に反対 → 冗長の反対＝簡潔なので simple and plain と一致。",
                                          "c：A number of Americans bemoan … と一致。d：make a career of it（それで身を立てる）＝professional success と一致。"]),
        ("6", "下線(2)の意味", "b", ["【推測】wannabe＝want to be、authoritarian＝authority の人、aplenty＝plenty → Many people want to …。",
                                  "though の前で「権威は存在しない」と言っているので、後ろは「でも権威者になりたがる人はたくさんいる」＝他人の言葉を統制したがる人が多い。"]),
        ("7", "下線(3)が示唆すること", "b", ["does not change＝dead を裏返すと change＝alive。vitality（生命力）は dead の反対、adapt over time は change の言い換え。"]),
        ("8", "controversy の発音を論じる理由", "c", ["unknown in the States, **being** a recent British innovation の分詞構文（理由）。",
                                              "[6] の主旨は「新しいもの＝アメリカ製、という思い込み」なので、その思い込みが外れている例として挙げている。"]),
        ("9", "下線(4)が含意すること", "c", ["**※ 間違えた問題。** 直後の It was **an illusion** based on misunderstandings が言い換え → chimera＝幻想。",
                                       "主語の「言語を fixed（固定）できるという希望」が immutability（im-＋mutable＝変わらないこと）にあたり、それが a myth（作り話）にすぎない、となる。",
                                       "d「英語は混成言語」は本文で話題になっていない。"]),
        ("10", "[11]〜[13] の要約", "b", ["[13] Rather, both American and British evolved in different ways の言い換え。",
                                      "a は Present-day British is no closer … than present-day American is と矛盾（むしろアメリカ英語のほうが保守的）。"]),
        ("11", "下線(5)を挙げる理由", "d", ["change from A（Old English）to B（computerspeak）は、昔から現在までの変化の流れ。has changed（現在完了）と最新の computerspeak から「今も変化中」。evolving は changed の言い換え。"]),
        ("12", "空所 A・B", "c（is not／plus）", ["前の not due to … と、後ろの Rather から、A は否定の is not。",
                                           "「アメリカ英語は、崩れたイギリス英語に野蛮な語を足したもの（plus）ではない」となるので B は plus。"]),
        ("13", "Adams の考えに NOT in line", "b", ["**※ 間違えた問題。** Adams はアメリカの人口増加と世界とのつながりが英語を広めると言っている（プラス要因）。b の「アメリカ人のせいで劣化する」は正反対。",
                                              "c・d は本文と一致。",
                                              "補足：a の「18〜19世紀」は、1780年から見れば「次とその次の世紀」なので厳密には19〜20世紀。ただし内容が正反対なのは b だけなので、答えは b。NOT 問題はまず「内容が逆転している選択肢」を探す。"]),
    ],
)

# ===========================================================================
# 大問Ⅱ
# ===========================================================================
P2 = dict(
    title="大問Ⅱ　なぜ「いい人すぎる人」は癪にさわるのか",
    flow=[
        ("[1]〜[3]", "現象の提示", "親切な善人をなぜか疑ってしまう。心理学では「do-gooder derogation（善人けなし）」と呼ぶ。進化上の理由がある。"),
        ("[4]〜[9]", "実験1", "公共財ゲームでは、ケチなただ乗りだけでなく、最も利他的な人も罰され、追い出された。8歳ごろから現れる、世界共通の傾向。"),
        ("[10]〜[16]", "理由", "利他性は評判を生むが、評判は「相対的（positional）」。他人の善行は自分の地位を下げるので、警戒・反感が生まれる。"),
        ("[17]〜[21]", "実験2", "利益が偶然なら問題ないが、利益が動機だと知ると「利己的」と評価が逆転する。私たちの疑いは直感にすぎず、正しいとは限らない。"),
        ("[22]〜[27]", "教訓", "他人には疑わしきは罰せず。自分の善行は控えめに。得をしたら正直に。最善はこっそり行い、誰かに見つけてもらうこと（Wilde）。"),
    ],
    sents=[
        ("[1]", "SVO（O が that 節）",
         "{M|<without any good reason to think so>}, {S|you} {Vt|suspect} {O|[that there {V'i|’s} {S'|something [ A ]} {M'|<about their altruism>}]}.",
         ["something＋形容詞は後ろから修飾（something calculated）。suspect that 〜「〜ではないかと疑う」はマイナスの内容を導く。→ 問2"],
         "とくに理由もないのに、彼らの利他的な行為には何か計算があるのではないかと疑ってしまう。"),
        ("[2]", "SVC（S が動名詞のカタマリ）",
         "{S|[{(V)|Finding} {(O)|yourself} {(C)|taking such an uncharitable attitude (towards people (who are only trying to make the world a better place))}]} {V|might feel} {C|uncomfortable}.",
         ["文頭の ing で、後ろに V（might feel）がある → ing のカタマリは名詞で S（tactics 028・041）。",
          "find O C（O が C しているのに気づく）のミクロ文型 (V)(O)(C)（tactics 034）。",
          "people who are **only** trying to make the world a better place → 善人に悪意はない（問14のヒント）。"],
         "世界をよくしようとしているだけの人々に、自分がそんな意地の悪い態度をとっていると気づくのは、落ち着かないことかもしれない。"),
        ("[5]", "SVOO の受身（O が1つ残る）",
         "{S|Participants} {V受|were then given} {O|the possibility (of {(V)|contributing} {(O)|some of that income} {(M)|<to a communal pool>} {(M)|<in each round of a game>})}.",
         ["give O₁ O₂ の受身 → O（the possibility）が1つ残る（tactics 018・022）。",
          "possibility＝「〜する可能性・選択肢」。出すかどうかは任意で、義務ではない。→ 問3"],
         "参加者はそれから、各ラウンドで、その所持金の一部を共同の資金に出す機会を与えられた。"),
        ("[6]", "SVO＋by doing（A and B）",
         "{S|Those (who are very stingy)}, however, {Vt|can game} {O|the system} {M|<by {(V)|paying} {(O)|very little} themselves and {(V)|reaping} {(O)|the rewards of others’ investments}>}.",
         ["by の後ろの paying と reaping を and が並べる（tactics 029）。game the system「制度を悪用する」。"],
         "しかし、ひどくケチな人は、自分はほとんど払わず他人の出資の利益を得ることで、仕組みを悪用できる。"),
        ("[7]", "SVOC（expect O to do）→ however で転換",
         "{M|<Given classic economic theory>}, {S|you} {Vt|might expect} {O|the stingy free-riders} {C|to receive those punishments} — and that was indeed the case. {M|[ B ]}, however, {S|the [ C ] altruistic participants} {V受|were also targeted} — {M|<even though {S'|they} {V'|were contributing} {O'|more than their fair share} {M'|<to the others’ riches>}>}.",
         ["expect O to do は SVOC（tactics 062）。O と C に主述関係（ただ乗りが罰を受ける）。",
          "however と also から、ここで「予想どおり」→「予想外」に転換する。B は驚きの語（Amazingly）。",
          "C は even though … more than their fair share と [8] the **extreme** altruists から most。→ 問5"],
         "古典的な経済理論からすれば、ケチなただ乗りが罰を受けると予想するだろうし、実際そうだった。ところが驚いたことに、最も利他的な参加者も標的にされた。彼らは他人の利益に、公平な分担以上の貢献をしていたにもかかわらず。"),
        ("[11]", "SVOC（help O to do）＋関係詞",
         "{M|<In the case of altruism>}, {S|[ D ] acts} {Vt|could help} {O|us} {C|to foster good relationships (within the group) (which ⟪S'欠⟫, <over time>, {V't|help} {O'|to build social capital and status})}.",
         ["help O to do「O が〜するのを助ける」。",
          "which の後ろの V' は help で、s が付いていない → 先行詞は複数の relationships（group ではない）。V の形で先行詞を決める。",
          "空所 D は In the case of altruism を受けて generous（気前のよい）。→ 問7"],
         "利他性の場合、気前のよい行為は集団内のよい関係を育むのに役立ち、その関係が時間とともに社会的な資本や地位を築くのに役立つのだ。"),
        ("[16]", "SVO（O の中が強調構文）",
         "{S|she} {Vt|found} {O|[△ {強調|it’s} often the highest (as well as the lowest) givers {強調|who} ⟪S'欠⟫ choose to remain anonymous]}.",
         ["found の後ろは that の省略（tactics 005①・024）。",
          "it’s 〜 who … は強調構文（tactics 095）。who の後ろは S が欠けた不完全文。"],
         "匿名を選ぶのは、最も少なく寄付する人だけでなく、最も多く寄付する人であることが多いと彼女はわかった。"),
        ("[21]", "SVO — and SVO＋when 節 → 言い換え",
         "{S|we} {V|are constantly trying to second-guess} {O|the reasons (for others’ actions)} — and {S|we} {Vt|punish} {O|people} {M|harshly} {M|<when {S'|we} {V't|suspect} {O'|[that their motives are impure]}>}. {S|Those instinctive suspicions} {V|may or may not be} {C|true}.",
         ["【推測】and の後ろの suspect と、次の文の Those instinctive **suspicions** が second-guess の言い換え → 「疑う」。→ 問9",
          "may or may not be true「正しいかもしれないし、そうでないかもしれない」→ 判断の根拠は直感。→ 問10"],
         "私たちは他人の行動の理由を絶えず勘ぐり、動機が不純だと疑うと厳しく罰する。もちろん、そうした本能的な疑いは正しいとは限らない。"),
        ("[22]", "SVOO（give O₁ O₂）＋分詞構文",
         "{M|<If there’s no good evidence (to suggest [that their acts of generosity are self-serving])>}, {S|we} {V|may choose to give} {O|them} {O|the benefit of the doubt}, {M|<{(V)|knowing} {(O)|[that our uncharitable intuitions may be fuelled by our own fears of losing status]}>}.",
         ["give O₁ the benefit of the doubt「（証拠がないので）O₁ を善意に解釈する」。",
          "knowing 〜 は分詞構文で、ミクロ S は文全体の S の we（tactics 040・052②）。→ 問8 b の根拠"],
         "彼らの善行が私利私欲のためだという確かな証拠がなければ、意地の悪い直感は自分の地位を失う恐れからきているかもしれないと心得て、善意に解釈することを選んでもよい。"),
        ("[23]", "if 節＋SVO",
         "And {M|<if {S'|people} {V't|bring} {O'|[ F ]} {M'|up}>}, {S|you} {V|should [ G ]} {O|them}, says Raihani.",
         ["bring O up「O を話題にする」。前の文の your good deeds を受けるので F＝them。",
          "前後の avoid noisily broadcasting（言いふらすな）と err on the side of modesty（控えめに）から G＝downplay。→ 問11"],
         "「人がそれを話題にしたら、控えめに扱うべきだ」とライハニは言う。"),
        ("[26]", "SVC（C が to do）",
         "{M|Ultimately}, {S|the only fool-proof way (to avoid do-gooder derogation)} {V|may be} {C|[to do your best deeds in complete secret]}.",
         ["S＝C（tactics 019）。「善人けなしを避ける唯一確実な方法＝完全に秘密で善行をすること」→ 問13 b の反証。"],
         "結局のところ、善人けなしを避ける唯一確実な方法は、最善の善行を完全に秘密で行うことかもしれない。"),
        ("[27]", "SVC（C が to do and (to) have O 原形）",
         "{S|The nicest feeling (in the world)} {V|is} {C|[to do a good deed anonymously — and (to) have somebody find out]}.",
         ["C は to do 〜 と (to) have O 原形 を and で並べたもの。have O do は使役（tactics 051）。",
          "anonymously（匿名で）＝自分からは言わない → 見せびらかさない。→ 問12"],
         "世界で最も素晴らしい気分は、匿名で善行をし、そして誰かにそれを見つけてもらうことだ。"),
    ],
    qs=[
        ("1", "do-gooder derogation が不可解な理由", "b", ["puzzling＝本文の seemingly irrational／wholly irrational。何が不合理かというと、[7] even though they were contributing more than their fair share to the others’ riches（他人に貢献しているのに罰される）こと。",
                                               "d は、経済理論が予測したのは「ただ乗りが罰される」ことで、「貢献者が報われる」とは書かれていない。"]),
        ("2", "空所 A", "a（calculated）", ["【推測】you suspect（疑う）なのでマイナスの内容。直前の too pleased with their good deeds（ご満悦すぎる）と [13] cunning and manipulative（ずる賢く操作的）から「善行の裏に計算がある」→ calculated。",
                                        "miscalculated（計算違い）、uncalculated（打算のない）、recalculated（再計算した）は「疑い」にならない。"]),
        ("3", "公共財ゲームについて NOT true", "a", ["本文は given the **possibility** of contributing（出すのは任意）。a の were **required** to（義務）が矛盾。",
                                             "b は [7][8] と一致（parsimonious＝stingy）。c は [9] universal tendency と一致。"]),
        ("4", "実験の並べ替え", "a（(3)→(2)→(4)→(1)）", ["[18] presented participants with various vignettes＝(3)、asked them to rate＝(2)。その後に結果の (1)[19] と (4)[20] が続く。(3)(2) で始まるのは a だけ。"]),
        ("5", "空所 B・C", "b（Amazingly／most）", ["however があるので、B は「予想どおり」の反対＝驚き（Expectedly は不可）。",
                                                  "C は even though … more than their fair share と [8] the **extreme** altruists から most。"]),
        ("6", "下線(1) hardwired", "b（inherent）", ["【推測】hard＋wired＝「配線が固定された」。文脈の evolved（進化した）と pass on our genes（遺伝子を受け継ぐ）から「遺伝的に組み込まれた＝生まれつきの」。"]),
        ("7", "空所 D", "c（generous）", ["直前の In the case of altruism（利他性の場合）を受ける → 利他的＝気前のよい行為。general／generic／genius は形の似た語のワナ。"]),
        ("8", "Carlson の実験から推論できるもの", "b と e", ["b：[21] Those instinctive suspicions may or may not be true と [22] give them the benefit of the doubt →「善人への反感は根拠がないこともある」。",
                                                     "e：[19][20] 同じ善行でも、利益が偶然か動機かで評価が逆転する → 人は結果よりも意図を見ている。",
                                                     "c は [17] we value integrity and honesty（誠実さも重視）と矛盾。"]),
        ("9", "下線(2) second-guess", "b（question or doubt）", ["【推測】and の後ろの we punish … when we **suspect** … は同じ方向の内容。次の文の Those instinctive **suspicions** も言い換え。",
                                                           "second（もう一度）＋guess（推測）＝「人の動機をあれこれ勘ぐる」。"]),
        ("10", "空所 E", "a（intuition rather than hard facts）", ["直前の Those **instinctive** suspicions may or may not be true から、判断の根拠は直感。[22] の our uncharitable **intuitions** も言い換え。"]),
        ("11", "空所 F・G", "c（them／downplay）", ["前文 avoid noisily broadcasting your good deeds、後文 err on the side of modesty。人が your good deeds を話題にしたら（bring them up）控えめに扱え（downplay）。us では「人が私たちを話題にしたら」で意味が通らない。"]),
        ("12", "下線(3)と合うもの", "b", ["anonymously（匿名で）＝自分では言わない → not … show off と一致。[26] the good reputation that follows is simply a bonus（評判は結果としてついてくるおまけ）と同じ趣旨。",
                                       "d「利他的な行為は必ず報われる」は言い過ぎ。"]),
        ("13", "記事について NOT true", "b", ["本文は [26] で do your best deeds in complete secret を勧めている。b の「秘密にするのは避けるべき」は正反対。"]),
        ("14", "rub you up the wrong way", "a（annoy you unintentionally）", ["猫の毛を逆向きになでる →「逆なでする」。",
                                                                            "【推測】善人は only trying to make the world a better place（よくしようとしているだけ）なのに、こちらは insufferable と感じる。悪意がないので「意図せずに」苛立たせる。辞書でもこの熟語は「意図せず人を苛立たせる」と説明されている。"]),
    ],
)

# ===========================================================================
# 大問Ⅲ
# ===========================================================================
P3 = dict(
    title="大問Ⅲ　パルテノン・マーブル論争（返還を主張するコラム）",
    flow=[
        ("[1]〜[2]", "導入（皮肉）", "スナク首相の子どもっぽい態度。国民は無関心で、半数以上は返還に賛成。英国にとっては学術的な口論だが、ギリシャにとっては深い恨み（非対称な論争）。"),
        ("[3]〜[6]", "反論つぶし", "法的所有権・保存の功績・見る人の数・複製で十分、という議論を一つずつ退ける。ギリシャ人にとっては「本物であること」が重要。"),
        ("[7]〜[9]", "批判", "帝国主義の後に残った傲慢さ。大博物館は他国の文化財を私物のように抱え込み、地下に眠らせている。"),
        ("[10]〜[11]", "結論", "世界は返還の流れにある（仏・独）。博物館は物を持ちすぎ。マーブルの返還はすぐれた前例になる。"),
    ],
    sents=[
        ("[1]", "SVO＋like 〜（M）",
         "{S|Rishi Sunak} {Vt|screeches} {O|“Mine, mine”} {M|<like a child (in a playground)>}.",
         ["【推測】screech を知らなくても、“Mine, mine”（ぼくの！）と like a child in a playground から駄々っ子のイメージ → demanding and immature。→ 問1"],
         "リシ・スナクは遊び場の子どものように「ぼくの、ぼくの」と金切り声をあげている。"),
        ("[1]", "SV — SVO（O の中は that 省略）",
         "{S|The nation} {Vi|[ A ]} — {S|polls} {Vt|show} {O|[△ {S'|over half} {V'|are} {C'|[ B ]} {M'|<to see the marbles returned>} and {S'|just above 20%} {V't|want} {O'|them} {C'|to stay}]}.",
         ["show の後ろは that の省略（tactics 005①・010）。",
          "over half are [B] と just above 20% want them to stay の対比 → 半数以上は返還に前向き＝happy。",
          "首相の大騒ぎに、野党党首は laughs、国民は yawns（あくび＝無関心）。→ 問2"],
         "国民はあくびをしている。世論調査では半数以上がマーブルの返還を喜んで受け入れ、残すべきだとするのは2割強にすぎない。"),
        ("[2]", "SVC（S が what のカタマリ）",
         "But {M|<as any visitor (to [ C ]) knows>}, {S|[what ⟪S'欠⟫ {M'|to [ D ]} {V'|is} {C'|a boring scholastic quarrel}]} {V|is} {M|to [ E ]} {C|a burning sense of grievance (that ⟪S'欠⟫ will not go away)}.",
         ["V は knows・is・is・will go の4つ、接続の役は as・what・that の3つで数が合う（V の数の法則：tactics 010）。",
          "what の中は S が欠けた不完全文（tactics 044）。「D にとっては退屈な学術的口論であるもの」が S。",
          "boring scholastic quarrel（持っている側）⇔ burning sense of grievance（奪われた側）の対比 → D＝Britain、E＝Greeks。恨みを知るのはギリシャを訪れた人 → C＝Greece。→ 問3"],
         "だがギリシャを訪れた人なら誰でも知っているように、英国にとっては退屈な学術的口論にすぎないものが、ギリシャ人にとっては消えることのない燃えるような恨みなのだ。"),
        ("[3]", "仮S真S＋but SVOC → And so what?",
         "{S|It} {V|is} {C|true} {S|[that {S'|more people} {V't|see} {O'|the marbles} {M'|in London} {M'|<than they would △ in Athens>}]}, but {S|they} {Vt|do not see} {O|them} {C|complete}. And so what?",
         ["It は仮主語、that 節が真主語。would の後ろは see them の省略。",
          "It is true that 〜, but …（確かに〜だが）の譲歩 → 反論。see O C は「O を C の状態で見る」→ 完全な形では見ていない。",
          "And so what?（それがどうした）で論点を切り捨てている。→ 問4"],
         "確かにアテネよりロンドンのほうがマーブルを見る人は多いが、完全な形で見ているわけではない。それがどうしたというのか。"),
        ("[5]", "仮定法の if 省略（倒置）",
         "{M|<Were {S'|the marbles} {V'受|cast} {M'|from bronze}, like St Mark’s horses in Venice or David in Florence>}, {S|they} {V受|could be copied} {M|over and again}.",
         ["仮定法で if を省略すると、条件部分が疑問文の語順（倒置）になる（tactics 005⑥）。＝ If the marbles were cast from bronze …。"],
         "もしマーブルがヴェネツィアのサン・マルコの馬やフィレンツェのダビデ像のようにブロンズで鋳造されていたら、何度でも複製できるだろう。"),
        ("[6]", "SVO ×3（Instead で対比）",
         "And {M|surely} {S|a [ F ] country (such as Britain)} {Vt|should have} {O|the [ G ] (to oblige)}. {S|It} {Vt|has} {O|the power (to restore integrity to this stupendous composition)} …. {M|Instead} {S|it} {Vt|humiliates} {O|itself} {M|<by taking umbrage over a cup of tea>}.",
         ["【推測】Instead it **humiliates** itself（その代わり自ら恥をさらしている）と対比 →「本来は品位を示すべきなのに」→ G＝dignity（humiliate の反対）。have the dignity to do「品位をもって〜する」。",
          "dignity と合う F は cultured（教養ある）。arrogance は [7] で筆者が批判する態度そのものなので不可。→ 問6"],
         "そして英国のような教養ある国なら、きっと品位をもって応じるべきだ。英国には、この壮大な作品の完全性を回復させる力がある。それなのに、お茶一杯のことで腹を立てて自ら恥をさらしているのだ。"),
        ("[8]", "SVOO（deny O₁ O₂）／as if の仮定法",
         "{S|They} {Vt|want to deny} {O|newly emergent countries} {O|the scope (to acquire similar collections)} {M|<by refusing to dispose or de-acquisition their vast reserves>}. {S|Many} {Vt|have} {O|the vast amount of their works} {M|<in store>}, {M|<as if {S'|they} {V'|were} {C'|the private property (of their custodians)}>}.",
         ["deny O₁ O₂「O₁ から O₂ を奪う・与えない」（tactics 022 の「奪う」シリーズ）。",
          "as if S' were 〜「まるで〜であるかのように」（事実は私物ではない）。fanatically reactionary とあわせて、博物館を「貪欲な保管者」と描いている。→ 問9"],
         "これらの施設は、膨大な所蔵品を手放すことを拒み、新興国が同様のコレクションを得る余地を奪おうとしている。多くの館は、まるで管理者の私物であるかのように、膨大な作品を倉庫にしまい込んでいる。"),
        ("[10]", "SV＋if not（たとえ〜でないにしても）",
         "{S|Museum walls} {Vi|are now crumbling} {M|ideologically} {M|<if not physically>}.",
         ["if not 〜「たとえ〜でないにしても」（if＋語：tactics 093）。「物理的には崩れていなくても、思想的には崩れつつある」という比喩。",
          "直後のフランス・ドイツの返還プログラムが具体例 → 従来の正当化が力を失っている。→ 問11"],
         "博物館の壁は、物理的にではないにしても、思想的には今や崩れつつある。"),
        ("[11]", "SVO＋関係詞 that（S 欠）",
         "{S|The V&A’s director, Tristram Hunt}, {M|<this week>} {Vt|floated} {O|a reform (of the 1983 National Heritage Act) (that ⟪S'欠⟫ {M'|at present} {V't|curbs} {O'|certain museums} {M'|<from “de-acquisitioning”>})}.",
         ["that の後ろの V' は curbs（三単現）→ 先行詞は単数の the 1983 National Heritage Act（tactics 031）。",
          "curb A from doing「A が〜するのを抑える」。"],
         "V&A 館長のトリストラム・ハントは今週、現在一部の博物館の「収蔵品の放出」を制限している1983年国家遺産法の改正を提案した。"),
    ],
    qs=[
        ("1", "screeches の含意", "b（demanding and immature）", ["“Mine, mine” と like a child in a playground から駄々っ子のイメージ。"]),
        ("2", "空所 A・B", "d（yawns／happy）", ["B：over half are [B] to see … returned と just above 20% want them to stay の対比 → 返還に前向き＝happy。",
                                                "A：首相の騒ぎに野党党首は laughs、国民は相手にしない → 退屈・無関心の yawns。"]),
        ("3", "空所 C・D・E", "d（Greece／Britain／Greeks）", ["boring scholastic quarrel ⇔ burning sense of grievance の対比。恨みを抱くのは奪われた側（E＝Greeks）、退屈な口論と思っているのは持っている側（D＝Britain）。その恨みを知るのはギリシャを訪れた人（C＝Greece）。直後の asymmetrical row（非対称な口論）とも一致。"]),
        ("4", "「ロンドンのほうが多くの人が見られる」という議論への態度", "c（無関係・誤解を招くとして退ける）", ["It is true that 〜, but … で譲歩 → they do not see them complete で反論 → And so what?（それがどうした）と切り捨て、ピラミッドの例で皮肉っている。"]),
        ("5", "複製と本物についての見解", "b", ["[5] reproduction can … appreciate the beauty（見た目は複製で足りる）。[6] But to the Greeks … this is indeed about **authenticity**（本物であることが重要）。But の前後で「見た目は OK、文化的意義は不十分」。"]),
        ("6", "空所 F・G", "a（cultured／dignity）", ["Instead it **humiliates** itself との対比 → 本来は品位（dignity）を示すべき。arrogance は筆者が批判する態度。"]),
        ("7", "[7] の筆者の意見", "d", ["筆者の評価は a post-imperial **arrogance** has crept into the debate。",
                                    "you may have got your independence back, but you are not getting your stuff 以降は、英国政府の言い分を真似た皮肉（it seems to say「〜と言っているようだ」）。a・b・c は皮肉として紹介された政府側の主張で、筆者の意見ではない。"]),
        ("8", "ギリシャと英国の見方の核心的な違い", "b", ["ギリシャ側：their ancestral temple、their crown jewels（最も大切なもの）＝象徴的な遺産。英国側：more people see them、a bigger show＝展示品・見せ物。"]),
        ("9", "大英博物館の描き方", "c（他文化の財産を貪欲に抱え込む存在）", ["[8] fanatically reactionary、refusing to dispose（手放さない）、as if they were the private property of their custodians（まるで私物のように）。"]),
        ("10", "マーブル保持論が誤っている理由", "c（法的な形式論にもとづいている）", ["[3] Of course Britain has legal title …, but laws can be changed で、「法的所有権」という形式論を退けている。b は [1] の世論調査（返還賛成が半数以上）と逆。"]),
        ("11", "下線(2)の意味", "b", ["if not physically＝「物理的にではないにしても」（tactics 093）。壁が実際に崩れているのではなく、ideologically に崩れている（比喩）。具体例が直後の仏・独の返還。a・d は物理的な崩壊なので不可。"]),
        ("12", "記事と NOT in line", "b", ["本文は This does not mean the death of the Louvre（ルーヴルが終わるわけではない）と言っているだけ。「ルーヴルに集中させるべき」は返還を主張する筆者の考えとも正反対。a は [3]、c は [9] vulnerable to theft and decay、d は [10] と一致。"]),
        ("13", "最適なタイトル", "a", ["最終段落 most museums have too much stuff と Returning the Parthenon marbles … an excellent one がそのままタイトルになっている。b は逆の主張、c は議論の紹介にとどまり筆者の返還論が出ていない、d は歴史の話。"]),
    ],
)

TIPS = [
    ("Ⅰ 問5", "fellow のような小さな語に国籍・立場の根拠が隠れている。人物の説明は所有格や fellow まで正確に読む。"),
    ("Ⅰ 問9", "知らない単語の直後に It was 〜 や that is のような言い換えがないか探す（chimera＝illusion）。"),
    ("Ⅰ 問13", "NOT 問題は、まず「内容が正反対の選択肢」を探す。細かい年代のズレより内容の逆転を優先する。"),
]

CSS_EXTRA = """
.flow-t { width:100%; border-collapse:collapse; font-size:9.8pt; margin-bottom:3mm; }
.flow-t td { border:1px solid #999; padding:1.2mm 2mm; vertical-align:top; }
.flow-t td.p { width:20mm; background:var(--soft); font-weight:bold; white-space:nowrap; }
.flow-t td.r { width:22mm; font-weight:bold; }
.ql { margin:0 0 3mm; break-inside:avoid; border-left:3px solid var(--ink); padding-left:3mm; }
.ql .qh { font-weight:bold; font-size:10.5pt; }
.ql .ans { display:inline-block; background:#fff1a6; border:1px solid #111; padding:0 2mm; margin-left:2mm; }
.ql ul { margin:.8mm 0 0; padding-left:1.2em; font-size:9.6pt; line-height:1.7; }
.tips td { border:1px solid #999; padding:1.2mm 2mm; font-size:10pt; }
.tips { border-collapse:collapse; width:100%; }
.tips td:first-child { width:22mm; font-weight:bold; background:var(--soft); white-space:nowrap; }
"""


def section(no, P):
    flow = "".join(f'<tr><td class="p">{html.escape(p)}</td><td class="r">{html.escape(r)}</td><td>{html.escape(t)}</td></tr>'
                   for p, r, t in P["flow"])
    sents = []
    for n, (para, pattern, ann, notes, ja) in enumerate(P["sents"], 1):
        li = "".join(f"<li>{md(x)}</li>" for x in notes)
        sents.append(f"""
<div class="sent">
  <div class="sn">{n}</div>
  <div class="pattern">{html.escape(para)}　{html.escape(pattern)}</div>
  <div class="en togi">{annotate_togi(ann)}</div>
  <ul class="notes">{li}</ul>
  <div class="ja"><span class="jt">訳</span>{html.escape(ja)}</div>
</div>""")
    qs = "".join(f"""
<div class="ql"><div class="qh">問{q}　{html.escape(t)}<span class="ans">{html.escape(a)}</span></div>
<ul>{''.join(f'<li>{md(x)}</li>' for x in xs)}</ul></div>""" for q, t, a, xs in P["qs"])
    return f"""
<section class="sec page">
  <h2><span class="num">{no}</span>{html.escape(P['title'])}</h2>
  <h3>段落の流れ（速読用）</h3>
  <table class="flow-t">{flow}</table>
  <h3>精読：設問に関わる文の構造</h3>
  {''.join(sents)}
</section>
<section class="sec page">
  <h3>設問解説（{html.escape(P['title'].split('　')[0])}）</h3>
  {qs}
</section>"""


def build():
    css = (HERE / "style.css").read_text() + CSS_EXTRA
    demo = annotate_togi("{S|S} {Vt|V} {O|O} {M|M}")
    tips = "".join(f"<tr><td>{html.escape(a)}</td><td>{html.escape(b)}</td></tr>" for a, b in TIPS)
    head = f"""
<div class="cover">
  <div class="kicker">英文読解戦略プリントで読む　精読 → 設問</div>
  <h1>2026年度 英語 <small>大問Ⅰ〜Ⅲ 解説</small></h1>
  <ol class="toc"><li>大問Ⅰ American English</li><li>大問Ⅱ do-gooder derogation</li><li>大問Ⅲ パルテノン・マーブル</li><li>間違えた問題から学ぶこと</li></ol>
</div>
<div class="legend togi">
  <div>{demo}　<b>主節</b>：黄色＝S・V・O・C（主役・中心・抽象）、緑色＝M（修飾語・具体・説明）（tactics 001・037）</div>
  <div>V の右下：<b>i</b>＝自動詞、<b>t</b>＝他動詞、<b>受</b>＝受身　<b>従属節</b>：S'・V'・O'・C'・M'（さらに内側は S''…）</div>
  <div><span class="gap">●</span>＝関係詞の内側で名詞が欠けている位置　△＝省略　(V)(O)(C)(M)＝準動詞のミクロ文型（tactics 034）</div>
  <div><span class="br">[ ]</span> 名詞のカタマリ　<span class="br">( )</span> 形容詞のカタマリ　<span class="br">&lt; &gt;</span> 副詞のカタマリ　【推測】＝単語を知らなくても解ける手がかり</div>
</div>
<h3>間違えた問題から学ぶこと（大問Ⅰ）</h3>
<table class="tips">{tips}</table>
"""
    body = head + section("Ⅰ", P1) + section("Ⅱ", P2) + section("Ⅲ", P3)
    OUT.write_text(f"""<!doctype html><html lang="ja"><head><meta charset="utf-8">
<title>2026年度 英語 解説</title><style>{css}
h2 .num {{ width:auto; padding:0 .4em; }}</style></head><body>{body}</body></html>""")
    print("wrote", OUT)


if __name__ == "__main__":
    build()
