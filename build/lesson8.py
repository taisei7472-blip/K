#!/usr/bin/env python3
"""第8講 演習問題 1・2 登木式 全文精読＋下線部和訳ポイント。PDF化: node render.js lesson8.html ../lesson8_explained.pdf"""
import html
import pathlib
import re

from build import annotate_togi

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "lesson8.html"
E = html.escape


def md(s):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", E(s))


# ===========================================================================
# 演習問題 1
# ===========================================================================
T1 = dict(
    title="演習問題1　子どもと演劇体験",
    flow=[
        ("第1〜2文", "導入", "幼い子を劇場に連れて行った親なら「演劇体験」の意味がわかるはず。劇場を理解しない幼児は舞台に怯える。"),
        ("第3文", "幼児の段階", "幼児は舞台を本当の出来事だと感じ、怖くなければ退屈で、寝たり遊んだりする。"),
        ("第4〜8文（下線1・2）", "1年後の段階", "「劇場にいて演技を見ている」とわかったうえで夢中になれる。舞台を味わいつつ、自分は安全な席にいると大人以上に意識している（二重の意識）。"),
        ("第9〜10文", "結論", "私たちを演劇の魔法に反応させるのは「内なる子ども」。子ども心を殺した大人は演劇を嫌う。"),
    ],
    sents=[
        ("SVO（O が what のカタマリ）",
         "{S|All parents (who ⟪S'欠⟫ {V'|have taken} {O'|young children} {M'|<to the theater>})} {V|must know} {M|exactly} {O|[what {S'|I} {V't|mean} ⟪O'欠⟫ {M'|<by dramatic experience>}]}.",
         ["who の中は S 欠（tactics 031）。V は must know（V の数の法則：tactics 010）。",
          "mean A by B「B で A を意味する」→ what I mean by 〜「〜という言葉で私が言おうとしていること」。what の中は mean の O が欠けている（tactics 044）。",
          "must は「〜にちがいない」（確信）。"],
         "幼い子どもを劇場に連れて行ったことのある親ならみな、私が「演劇体験」という言葉で何を言おうとしているのか、きっとよくわかるはずだ。"),
        ("SV（受身）",
         "{S|Very small children (who ⟪S'欠⟫ {V'|do not understand} {M'|<about theaters>})} {V受|are} {M|soon} {V受|frightened} {M|<by [what {S'|they} {V't|see} ⟪O'欠⟫ {M'|<on the stage>}]>}.",
         ["S が長いので V（are frightened）を見つけて区切る（tactics 036）。be frightened「怖がる」（tactics 086）。",
          "by の後ろの what のカタマリは名詞（前置詞の O）。see の O が欠けている。"],
         "劇場というものがわからないとても幼い子どもは、舞台で目にするものにすぐ怯えてしまう。"),
        ("SVO, and SVC＋so that（結果）",
         "{S|They} {Vt|feel} {O|[△ {S'|it} {V'|is} {M'|really} {V'|happening}]}, and {M|<when {S'|it} {V'|is not} {C'|alarming}>} {S|it} {V|is} {M|merely} {C|dull} {M|<to them>}, {M|<so that {S'|they} {V'i|go} {M'|<to sleep>} or {V'|want to ignore} {O'|it} and {V'i|play} {M'|<with something>}>}.",
         ["feel の後ろは that の省略（tactics 005①・024）。V が feel・is happening・is・is と多いのに接続詞が見えない → △ を補う（tactics 010）。",
          "when it is not alarming「怖くないときは」→ 怖い ⇔ 退屈 の二択。",
          "カンマ＋so that は「その結果〜」（結果）。go to sleep と want to ignore … and play を or が並べる（tactics 029）。"],
         "彼らはそれが本当に起きていると感じ、怖くないときには単に退屈なだけなので、眠ってしまったり、舞台を無視して何かで遊びたがったりする。"),
        ("SV＋to the idea [that …]（下線部(1)）",
         "{M|<A year later>} {S|these same children} {V|may be able to cling} {M|safely} {M|<to the idea [that {S'|they} {V'|are} {M'|<in a theater>}, {M'|<{(V)|watching} {(O)|people} {(C)|pretend}>}]>}, {M|<while {(M)|excitedly} {(V)|following} {(O)|the action (on the stage)}>}.",
         ["cling to 〜「〜にしがみつく」。the idea that 〜 は同格の that（中は完全文：tactics 033②）。",
          "watching people pretend は分詞構文。watch O 原形「O が〜するのを見る」（知覚動詞：tactics 062）。pretend「ふりをする」→ 演技をする。",
          "while ＋いきなり ing（tactics 113）＝ while they are excitedly following …。"],
         "1年後には、この同じ子どもたちが、自分は劇場にいて人々が演技をしているのを見ているのだという考えを安心して保ちながら、舞台の展開にわくわくしてついていけるようになるかもしれない。"),
        ("SVC＋同格",
         "{M|Then} {S|they} {V|are} {C|enchanted and delighted}, {C|a wonderful audience}.",
         ["be＋感情の p.p.（enchanted・delighted）は SVC で読める（tactics 086①）。",
          "a wonderful audience は they を言い換えた同格的な補足。"],
         "そうなると子どもたちは魅了され、大喜びする。すばらしい観客なのだ。"),
        ("仮S真S（why の後ろの省略）",
         "And {S|it} {V|is} {C|easy} {S|[to see why △]}.",
         ["it は仮主語、to see why が真主語。why の後ろは they are enchanted and delighted の省略。"],
         "そして、その理由は容易にわかる。"),
        ("SVC",
         "{S|Children} {V|are} {C|fully responsive} {M|<on each level>}.",
         ["responsive「反応がよい」。on each level「どの次元でも」→ 次の文の Not only A but B で「2つの次元」を説明する予告。"],
         "子どもたちは、どの次元においても十分に反応するのだ。"),
        ("Not only 倒置＋but SVC（下線部(2)）",
         "{M|Not only} {V|do} {S|they} {Vt|appreciate} {M|<to the full>} {O|[what ⟪S'欠⟫ {V'|is happening} {M'|<on the stage>}]}, but {M|<at the same time>} {S|they} {V|are} {M|even more intensely} {C|conscious} {M|<than adults are △>} {M|<of [not {(V)|being} {(M)|physically} {(C)|involved} {(M)|<in the scene>}]>}, {M|<of [{(V)|sitting} {(M)|safely and comfortably} {(M)|<in the seat (by the side of Mommy)>}]>}.",
         ["否定の副詞（Not only）が文頭 → 疑問文の語順（倒置）：do they appreciate（tactics 087）。",
          "appreciate O の O（what 節）が長いので、M（to the full）が V と O の間に入っている。",
          "be conscious of A「A を意識している」。2つの of 〜 は同じカタチの並列で、2つめは1つめの言い換え。",
          "even more ＋原級＝比較級の強調（tactics 105）。than adults are △ は conscious の省略。"],
         "子どもたちは舞台で起きていることを存分に味わうだけでなく、同時に、自分がその場面に実際に身を置いているわけではないこと、つまりママのそばの座席に安全に心地よく座っていることを、大人以上にずっと強く意識しているのだ。"),
        ("It may be that 〜（中が強調構文）",
         "So {M|<it may well be that>} {強調|it is} {S'|the child (in us)} {強調|who} ⟪S'欠⟫ {V't|makes} {O'|us} {C'|responsive} {M'|<to this magic>}.",
         ["It may (well) be that 〜「たぶん〜だろう」は文頭の M とみなす（tactics 110）。",
          "it is 〜 who … は強調構文（tactics 095）。make O C「O を C にする」（SVOC：tactics 062）。"],
         "だから、私たちをこの魔法に反応させるのは、おそらく私たちの中にいる子どもなのだろう。"),
        ("長い S（関係詞 who ×2）＋V and V",
         "{S|Men and women (who ⟪S'欠⟫ {V'|are} {M'|completely} {C'|removed} {M'|<from their childhood>}), (who ⟪S'欠⟫ {M'|<for one reason or another>} {V'|have had to take} {O'|the child (in them)} and {V't|wring} {O'|its neck})} {M|generally} {Vt|dislike} {O|the Theater} and {V|are} {C|reluctant and unresponsive playgoers}.",
         ["S に who 節が2つ（2つめはカンマつきの補足）。主節の V は dislike と are（tactics 010・029）。",
          "wring its neck「その首を絞める」→ 内なる子どもを殺してしまう、という比喩。"],
         "子ども時代から完全に切り離され、何らかの理由で自分の中の子どもをつかまえてその首を絞めなければならなかった大人の男女は、たいてい演劇が嫌いで、気が進まず反応の鈍い観客なのである。"),
    ],
    underlines=[
        dict(no="問1　下線部(1)", en="A year later these same children may be able to cling safely to the idea that they are in a theater, watching people pretend, while excitedly following the action on the stage.",
             points=[
                 ("these same children", "「この同じ子どもたち」。前の文の「劇場を理解せず怖がる幼児」と同じ子が1年後に変わる、という対比。same を落とさない。"),
                 ("may be able to do", "「〜できるようになるかもしれない」。may（可能性）と be able to（能力）を両方訳す。"),
                 ("cling safely to the idea that 〜", "直訳「〜という考えに安全にしがみつく」→「〜という考えを安心して（しっかり）持ち続ける」。that 節は idea の中身（同格）。"),
                 ("watching people pretend", "watch O 原形「O が〜するのを見る」。pretend は「ふりをする」→ 劇の文脈なので「演技をする」。「人々が演技しているのを見ている」。"),
                 ("while excitedly following 〜", "while ＋ ing＝ while they are following。「〜しながら」。excitedly「わくわくして」。the action on the stage「舞台上の出来事・展開」（action は「行動」より「劇の筋の展開」）。"),
                 ("訳の要", "①「これは劇だ」とわかっている意識と、②夢中になってついていく意識が同時にある、という二重性が伝わるように訳す。"),
             ],
             model="1年後には、この同じ子どもたちが、自分は劇場にいて人々が演技をしているのを見ているのだという考えを安心して持ち続けながら、わくわくして舞台の展開を追うことができるようになるかもしれない。"),
        dict(no="問2　下線部(2)", en="Not only do they appreciate to the full what is happening on the stage, but at the same time they are even more intensely conscious than adults are of not being physically involved in the scene, of sitting safely and comfortably in the seat by the side of Mommy.",
             points=[
                 ("Not only do they appreciate", "否定の副詞が文頭 → 倒置（tactics 087）。Not only A but (also) B「A だけでなく B も」。do は訳さない。"),
                 ("appreciate to the full what 〜", "appreciate O to the full の O（what 節）が後ろに回った形。「〜を存分に味わう・十分に理解する」。appreciate は「感謝する」ではない。"),
                 ("even more intensely conscious than adults are of 〜", "be conscious of A「A を意識している」が骨格。比較の than adults are が間に挟まっている → of 〜 を conscious につなぐのが最大のポイント。even more「（大人より）さらにいっそう」。"),
                 ("of not being physically involved in the scene", "動名詞の否定は not を ing の前に置く。「その場面に身体的に巻き込まれていないこと」→「実際にはその場面に身を置いていないこと」。"),
                 (", of sitting safely …", "2つめの of は1つめの言い換え（同じカタチの並列）。「つまり〜していること」とつなぐと自然。"),
                 ("by the side of Mommy", "「ママのそばで」。Mommy は幼児語なので「ママ」と訳すと雰囲気が出る。"),
             ],
             model="子どもたちは舞台で起きていることを存分に味わうだけでなく、同時に、自分がその場面に実際に身を置いているわけではないこと、つまりママのそばの座席に安全に心地よく座っていることを、大人以上にずっと強く意識しているのだ。"),
    ],
)

# ===========================================================================
# 演習問題 2
# ===========================================================================
T2 = dict(
    title="演習問題2　男もうわさ話をする（Watching the English）",
    flow=[
        ("第1〜3文", "一般論の否定", "通念に反し、男性も女性と同じくらいうわさ話をする（会話の55〜67％）。差はサッカーの話で説明できる程度。"),
        ("第4〜6文（下線1・2）", "例外", "男性が「高尚な」話題を話すのは、女性がいて良く見せたいときだけ。男性だけだと高尚な話題は5％以下。"),
        ("第7〜8文", "唯一の違い", "男性は自分自身のことを話す時間が長い。"),
        ("第9文（下線3）", "それでも残る俗説", "「男は世界の問題を論じ、女は台所でうわさ話」という神話が、特に男性の間で信じられている。"),
        ("第10〜12文（下線4・5）", "違いの正体", "男性は「うわさ話はしない」と言うが、実は呼び方の違い。男性はうわさ話を「情報交換」と呼ぶ。うわさ話は不名誉だから別の名前で呼ぶという不文律。"),
        ("第13〜14文", "結論", "さらに大事なのは「うわさ話に聞こえない」こと。男女の違いは、女性のうわさ話が実際にうわさ話らしく聞こえる点にある。"),
    ],
    sents=[
        ("SVO（O が that 節）",
         "{M|<Contrary to popular belief>}, {S|researchers} {V|have found} {O|[that {S'|men} {V'i|gossip} {M'|<just as much as women>}]}.",
         ["Contrary to popular belief「一般に信じられているのとは反対に」→ 一般論を否定して筆者の主張を出す合図。",
          "find that 〜「〜とわかる」（tactics 024）。just as much as 〜「〜とまったく同じくらい」。"],
         "一般に信じられているのとは反対に、男性も女性とまったく同じくらいうわさ話をすることを研究者たちは発見した。"),
        ("SVO＋to 〜 ; SV受C＋with O ing",
         "{M|<In one English study>}, {S|both sexes} {Vt|devoted} {O|the same amount of conversation time (about 65 per cent)} {M|<to social topics (such as personal relationships)>}; {M|<in another △>}, {S|the difference} {V受|was found} {C|to be quite small}, {M|<with {(S)|gossip} {(V)|accounting for} {(O)|55 per cent of male conversation time and 67 per cent of female △ time}>}.",
         ["devote A to B「A を B に費やす」。one 〜 ; another 〜「ある研究では…、別の研究では…」（another の後ろに study の省略）。",
          "find O to be C の受身 → C が残る（tactics 018）。",
          "with O ing は付帯状況「O が〜していて」。account for は「（割合を）占める」。"],
         "ある英国の研究では、男女とも会話時間の同じ量（約65％）を個人的な人間関係などの社会的な話題に費やしていた。別の研究では差はごく小さく、うわさ話は男性の会話時間の55％、女性の67％を占めていた。"),
        ("As 節（理由）＋SVO",
         "{M|<As {S'|sport and leisure} {V'受|have been shown} {C'|to occupy about 10 per cent of conversation time}>}, {S|discussion (of football)} {V|could well account for} {O|the difference}.",
         ["as は理由「〜なので」（tactics 111②）。show O to do の受身 → to do が残る。",
          "could well do「十分〜しうる」。account for は今度は「〜の原因となる・説明する」。直前の文の account for（占める）と意味が違う点に注意。"],
         "スポーツと余暇が会話時間の約10％を占めることが示されているので、サッカーの話題でその差は十分に説明がつくだろう。"),
        ("SVOC の受身＋no more 〜 than（下線部(1)）",
         "{S|Men} {V受|were certainly found} {C|to be no more likely (than women) to discuss “important” or “sophisticated” subjects (such as politics, work, art and cultural matters)} — {M|<except (and this was a striking difference) when {S'|women} {V'|were} {C'|present}>}.",
         ["find O to be C の受身 → S was found to be C「S は C だとわかった」（tactics 018）。",
          "no more 〜 than …「…と同じく〜ない」。比較の両方を否定する（no＋比較級）。be likely to do「〜しがちだ」。",
          "except when 〜「〜のときを除いて」。( ) は挿入。"],
         "確かに、男性が政治、仕事、芸術、文化的な事柄といった「重要な」あるいは「高尚な」話題を論じる傾向は、女性と比べて少しも高くないことがわかった。ただし――これは際立った違いだったが――女性がその場にいるときは別である。"),
        ("SV＋with O p.p.（no more than＝only）",
         "{M|<On their own>}, {S|men} {Vi|gossip}, {M|<with {(S)|no more than five per cent of conversation time} {(V受)|devoted} {(M)|<to non-social subjects (such as work or politics)>}>}.",
         ["on their own「男性だけでいるとき」。",
          "with O p.p.「O が〜されて」（付帯状況）。no more than ＝ only「たった〜」。下線(1)の no more likely than と区別する。"],
         "男性だけでいるときは、男性はうわさ話をし、仕事や政治といった社会的でない話題に費やされる会話時間はわずか5％にすぎない。"),
        ("強調構文 It is only 〜 that …（下線部(2)）",
         "{強調|It is} only {M|<in mixed-sex groups, (where there are women (to impress))>}, {強調|that} {S'|the proportion (of male conversation time) (devoted to these more “sophisticated” subjects)} {V'i|increases} {M'|dramatically}, {M'|<to between 15 and 20 per cent>}.",
         ["It is 〜 that … の強調構文（tactics 095）。that の後ろは完全文（S'＋V'i）で、前に出た M を強調している。",
          ", where は非制限の関係副詞（中は完全文）。women to impress「（男性が）印象づけたい女性」：to do が前の名詞にかかり、impress の O が women。",
          "devoted は過去分詞で time にかかる（tactics 013）。V' は increases（三単現 → S' は proportion）。"],
         "男性の会話時間のうち、こうしたより「高尚な」話題に費やされる割合が劇的に増えて15〜20％にまでなるのは、良く見せたい女性がいる男女混合の集団においてだけである。"),
        ("SVO＋コロンで具体化",
         "{M|<In fact>}, {S|recent research} {V|has revealed} {O|only one significant difference, <in terms of content>, (between male and female gossip)}: {S|men} {Vt|spend} {O|much more time} {M|<talking about themselves>}.",
         ["in terms of 〜「〜の点で」が O の中に挿入されている。between 〜 は difference にかかる。",
          "コロンの後ろが one significant difference の中身。spend time doing「〜して時間を過ごす」。much は比較級の強調。"],
         "実のところ、最近の研究で明らかになった男女のうわさ話の内容面での大きな違いは一つだけだ。男性のほうが自分自身について話す時間がずっと長いのである。"),
        ("Of 〜（〜のうち）＋SVO, while SV",
         "{M|<Of the total time (devoted to conversation about social relationships)>}, {S|men} {Vt|spend} {O|two thirds} {M|<talking about their own relationships>}, {M|<while {S'|women} {M'|only} {V'i|talk} {M'|<about themselves>} {M'|one third of the time}>}.",
         ["文頭の Of 〜「〜のうち」。while は対比「一方」。"],
         "人間関係についての会話に費やされる時間全体のうち、男性は3分の2を自分自身の人間関係について話すのに使うが、女性が自分のことを話すのは3分の1にすぎない。"),
        ("SV受＋離れた同格 that（下線部(3) the myth）",
         "{M|<Despite these findings>}, {S|the myth} {V受|is} {M|still} {M|widely} {V受|believed}, {M|<particularly among males>}, {M|[that {S'|men} {V't|spend} {O'|their conversations} {M'|“solving the world’s problems,”} {M'|<while the womenfolk gossip in the kitchen>}]}.",
         ["the myth と同格の that 節が、V（is believed）の後ろに離れて置かれている。S が長くなりすぎるのを避けた形。the myth の中身＝that 以下。",
          "Despite these findings「これらの研究結果にもかかわらず」→ myth は事実に反する「俗説」。",
          "spend O doing「O を〜して過ごす」。“ ” つきの solving the world’s problems は皮肉（大げさな表現）。"],
         "これらの研究結果にもかかわらず、男性は会話を「世界の問題の解決」に費やし、その間女たちは台所でうわさ話をしている、という神話は、特に男性の間でいまだに広く信じられている。"),
        ("SVO, while SVO（代動詞 did）",
         "{M|<In my focus groups and interviews>}, {S|most English males} {M|initially} {Vt|claimed} {O|[that they did not gossip]}, {M|<while {S'|most of the females} {M'|readily} {V't|admitted} {O'|[that they did △]}>}.",
         ["did＝gossiped（代動詞）。initially「当初は」→ 次の文の however（さらに聞くと）を予告。"],
         "私のフォーカス・グループや面接では、イングランドの男性のほとんどが当初はうわさ話などしないと主張したが、女性のほとんどはすぐにしていると認めた。"),
        ("SV（turn out to be）: OSV（下線部(4)）",
         "{M|<On further questioning>}, however, {S|the difference} {V|turned out to be} {C|more a matter of language than of practice}: {O|[what {S'|the women} {V'|were happy to call} ⟪O'欠⟫ {C'|“gossip,”}]} {S|the men} {Vt|defined} {M|as “exchanging information.”}",
         ["on doing「〜すると」。turn out to be C「C だとわかる」（まとめて V：tactics 017）。",
          "more A than B「B というよりむしろ A」。language（呼び方）⇔ practice（実際の行い）の対比。",
          "コロン以下は O が文頭に出た OSV（tactics 030 の例外パターン）。define A as B の A（what 節）が前に出ている。what の中は call O C の O が欠けている（tactics 044）。"],
         "しかし、さらに質問していくと、その違いは実際の行動というよりむしろ言葉の問題であることがわかった。女性たちが平気で「うわさ話」と呼ぶものを、男性たちは「情報交換」と定義していたのである。"),
        ("There＋V＋S＋同格（下線部(5)）",
         "{M|Clearly}, there {Vi|is} {S|a sense of dishonor (attached to gossip among English males), an unwritten rule (to the effect [that, <even if [what {S''|one} {V''|is doing} ⟪O''欠⟫] is gossiping>, {S'|it} {V'受|should be called} {C'|something else}])}.",
         ["attached to 〜 は過去分詞で前の名詞にかかる（tactics 013）。a sense of dishonor attached to 〜「〜に結びついた不名誉の感覚」。",
          "an unwritten rule は a sense of dishonor の言い換え（同格：tactics 003）。",
          "to the effect that 〜「〜という趣旨の」（that は同格）。what one is doing「自分のしていること」は what 節が S。"],
         "明らかに、イングランドの男性の間ではうわさ話に不名誉の感覚がつきまとっている。それは、たとえ自分のしていることがうわさ話であっても、何か別の名前で呼ばれるべきだという不文律である。"),
        ("省略文（C ＋コロン）",
         "Perhaps {C|even more important}: {S|it} {V|should sound} {C|like something else}.",
         ["(What is) even more important (is this): の省略。sound like 〜「〜のように聞こえる」。"],
         "おそらくさらに重要なのは、それが何か別のものに聞こえなければならない、ということだ。"),
        ("SVO（O の中が SVC＋that 節）",
         "{M|<In my gossip research>}, {S|I} {Vt|found} {O|[that {S'|the main difference (between male and female gossip)} {V'|is} {C'|[that female gossip actually sounds like gossip]}]}.",
         ["is の後ろの that 節は C（tactics 028）。actually「実際に」→ 男性のうわさ話はうわさ話に聞こえないように話されている、という含み。"],
         "うわさ話の研究で私がわかったのは、男女のうわさ話の主な違いは、女性のうわさ話は実際にうわさ話のように聞こえる、という点だということだ。"),
    ],
    underlines=[
        dict(no="問1　下線部(1)", en="Men were certainly found to be no more likely than women to discuss “important” or “sophisticated” subjects such as politics, work, art and cultural matters — except (and this was a striking difference) when women were present.",
             points=[
                 ("were found to be 〜", "find O to be C の受身。「〜だとわかった」。「見つけられた」は×。"),
                 ("no more likely than women to discuss 〜", "no＋比較級＝「…と同様に〜でない」。直訳「女性より少しも〜しがちではない」→「男性が〜を論じる傾向は女性と比べて少しも高くない」。「女性ほど〜しない」と訳すと逆の意味になるので×。"),
                 ("“important” or “sophisticated”", "“ ” 付きは「いわゆる」のニュアンス。「『重要な』あるいは『高尚な』」とかぎかっこを残す。"),
                 ("except … when women were present", "except when 〜「〜のときを除いて」。「ただし、女性がその場にいるときは別だ」と文を分けると自然。"),
                 ("(and this was a striking difference)", "挿入。「そしてこれは際立った違いだったのだが」。訳から落とさない。"),
             ],
             model="確かに、男性が政治、仕事、芸術、文化的な事柄といった「重要な」あるいは「高尚な」話題を論じる傾向は、女性と比べて少しも高くないことがわかった。ただし――そしてこれは際立った違いだったのだが――女性がその場にいるときは別である。"),
        dict(no="問2　下線部(2)", en="It is only in mixed-sex groups, where there are women to impress, that the proportion of male conversation time devoted to these more “sophisticated” subjects increases dramatically, to between 15 and 20 per cent.",
             points=[
                 ("It is only 〜 that …", "強調構文（tactics 095）。「…するのは〜においてだけだ」と、強調部分（only in mixed-sex groups）を文末に置いて訳すのが定石。「〜で初めて…」も可。"),
                 ("where there are women to impress", "非制限の関係副詞。women to impress は「（男性が）良いところを見せたい女性」。impress の O が women。「印象づける女性」だと女性が主語に見えるので注意。"),
                 ("the proportion of male conversation time devoted to 〜", "S の中心は proportion。devoted to 〜 は time にかかる。「〜に費やされる男性の会話時間の割合」。"),
                 ("increases dramatically, to between 15 and 20 per cent", "increase to 〜「〜にまで増える」。between A and B が to の O になった形。「劇的に増えて15〜20％にもなる」。"),
             ],
             model="男性の会話時間のうち、こうしたより「高尚な」話題に費やされる割合が劇的に増えて15〜20パーセントにまでなるのは、良いところを見せたい女性がいる男女混合の集団においてだけである。"),
        dict(no="問3　下線部(3) the myth の内容説明", en="Despite these findings, the myth is still widely believed, particularly among males, that men spend their conversations “solving the world’s problems,” while the womenfolk gossip in the kitchen.",
             points=[
                 ("中身はどこか", "the myth と同格の that 節が、V（is believed）の後ろに離れて置かれている。the myth の内容＝that 以下。S が長くなりすぎるので that 節を後ろに回した形。"),
                 ("“solving the world’s problems”", "かぎかっこ付きの大げさな表現。具体的には、第4文の政治・仕事・芸術・文化といった「重要な・高尚な話題」を論じること。説明問題では本文の言い換えまで具体化する。"),
                 ("while the womenfolk gossip in the kitchen", "while は対比「一方で」。womenfolk は「女たち」（やや古い言い方）。"),
                 ("myth のニュアンス", "Despite these findings があるので、「研究結果に反する、根拠のない俗説」であることも答えに含めるとよい。"),
             ],
             model="【解答例】男性は会話の時間を政治や仕事などの「世界の問題」を解決するような高尚な話題に費やしているのに対し、女性たちは台所でうわさ話ばかりしている、という（研究結果に反するのに、特に男性の間で広く信じられている）俗説。"),
        dict(no="問4　下線部(4)", en="On further questioning, however, the difference turned out to be more a matter of language than of practice: what the women were happy to call “gossip,” the men defined as “exchanging information.”",
             points=[
                 ("On further questioning", "on doing「〜すると」。「さらに質問すると・さらに問いただしてみると」。"),
                 ("turned out to be 〜", "「〜だとわかった・判明した」。"),
                 ("more a matter of language than of practice", "more A than B「B というよりむしろ A」。language は「言語」より「言葉（呼び方）」、practice は「練習」ではなく「実際の行い・実践」。"),
                 ("what the women … , the men defined as …", "O が文頭に出た OSV（define A as B の A が前）。「女性が〜と呼ぶものを、男性は…と定義していた」と、O から訳すと語順のまま自然に訳せる。"),
                 ("were happy to call", "be happy to do「喜んで（平気で）〜する」。「幸せ」は×。"),
             ],
             model="しかし、さらに質問していくと、その違いは実際の行動というよりむしろ言葉の問題であることがわかった。女性たちが平気で「うわさ話」と呼ぶものを、男性たちは「情報交換」と定義していたのである。"),
        dict(no="問5　下線部(5)", en="Clearly, there is a sense of dishonor attached to gossip among English males, an unwritten rule to the effect that, even if what one is doing is gossiping, it should be called something else.",
             points=[
                 ("a sense of dishonor attached to gossip", "attached to 〜 は過去分詞の後置修飾。「うわさ話につきまとう不名誉の感覚」→「うわさ話は不名誉なものだという感覚」。"),
                 ("among English males", "「イングランドの男性の間で」。"),
                 ("an unwritten rule", "a sense of dishonor の言い換え（同格）。「すなわち〜という不文律」とつなぐ。"),
                 ("to the effect that 〜", "「〜という趣旨の」。that 以下が rule の中身。"),
                 ("even if what one is doing is gossiping", "what 節が S。one は一般の人「自分」。「たとえ自分のしていることがうわさ話であっても」。"),
                 ("it should be called something else", "「それは何か別の名前で呼ばれるべきだ」。something else「何か別のもの」。"),
             ],
             model="明らかに、イングランドの男性の間では、うわさ話には不名誉な感覚がつきまとっている。すなわち、たとえ自分のしていることがうわさ話であっても、それは何か別の名前で呼ばれなければならない、という不文律があるのだ。"),
    ],
)

CSS_EXTRA = """
.flow-t { width:100%; border-collapse:collapse; font-size:9.8pt; margin-bottom:3mm; }
.flow-t td { border:1px solid #999; padding:1.2mm 2mm; vertical-align:top; }
.flow-t td.p { width:34mm; background:var(--soft); font-weight:bold; }
.flow-t td.r { width:24mm; font-weight:bold; }
.ul { border:1.5px solid var(--ink); padding:3mm 4mm; margin:0 0 4mm; }
.ul .uh { font-weight:bold; font-size:11pt; margin-bottom:1.5mm; }
.ul .uen { font-family:"Liberation Serif",serif; font-size:11pt; line-height:1.7; background:#fff8cc; padding:1.5mm 2.5mm; margin-bottom:2mm; }
table.pt { width:100%; border-collapse:collapse; font-size:9.6pt; margin-bottom:2mm; }
.pt td { border:1px solid #999; padding:1mm 2mm; vertical-align:top; }
.pt td.k { width:52mm; font-family:"Liberation Serif",serif; font-weight:bold; background:var(--soft); }
.model { border-left:4px solid #b3261e; background:#fdf1f0; padding:2mm 3mm; font-size:10.2pt; line-height:1.85; }
.model b { color:#b3261e; }
"""


def section(no, T):
    flow = "".join(f'<tr><td class="p">{E(p)}</td><td class="r">{E(r)}</td><td>{E(t)}</td></tr>' for p, r, t in T["flow"])
    sents = "".join(f"""
<div class="sent">
  <div class="sn">{n}</div>
  <div class="pattern">{E(pat)}</div>
  <div class="en togi">{annotate_togi(ann)}</div>
  <ul class="notes">{''.join(f'<li>{md(x)}</li>' for x in notes)}</ul>
  <div class="ja"><span class="jt">訳</span>{E(ja)}</div>
</div>""" for n, (pat, ann, notes, ja) in enumerate(T["sents"], 1))
    uls = "".join(f"""
<div class="ul">
  <div class="uh">{E(u['no'])}</div>
  <div class="uen">{E(u['en'])}</div>
  <table class="pt">{''.join(f'<tr><td class="k">{E(k)}</td><td>{md(v)}</td></tr>' for k, v in u['points'])}</table>
  <div class="model"><b>模範訳</b>　{E(u['model'])}</div>
</div>""" for u in T["underlines"])
    tr = "".join(s[3] for s in T["sents"])
    return f"""
<section class="sec page">
  <h2><span class="num">{no}</span>{E(T['title'])}</h2>
  <h3>文章の流れ（速読用）</h3>
  <table class="flow-t">{flow}</table>
  <h3>精読：全文の構造</h3>
  {sents}
</section>
<section class="sec page">
  <h3>下線部の訳のポイント</h3>
  {uls}
  <h3>全訳</h3>
  <div class="translation"><p>{E(tr)}</p></div>
</section>"""


def build():
    for T in (T1, T2):
        for s in T["sents"]:
            assert s[1].count("{") == s[1].count("}"), s[1]
    css = (HERE / "style.css").read_text() + CSS_EXTRA
    demo = annotate_togi("{S|S} {Vt|V} {O|O} {M|M}")
    head = f"""
<div class="cover">
  <div class="kicker">英文読解戦略プリントで読む　全文精読 → 下線部和訳</div>
  <h1>第8講 演習問題 <small>1 子どもと演劇体験／2 男もうわさ話をする</small></h1>
</div>
<div class="legend togi">
  <div>{demo}　<b>主節</b>：黄色＝S・V・O・C、緑色＝M（tactics 001・037）。V の右下：i＝自動詞、t＝他動詞、受＝受身</div>
  <div><b>従属節</b>：S'・V'…　<span class="gap">●</span>＝欠けている位置　△＝省略　(V)(O)(C)(M)＝準動詞のミクロ文型（tactics 034）</div>
  <div><span class="br">[ ]</span> 名詞のカタマリ　<span class="br">( )</span> 形容詞のカタマリ　<span class="br">&lt; &gt;</span> 副詞のカタマリ</div>
</div>"""
    body = head + section("1", T1) + section("2", T2)
    OUT.write_text(f"""<!doctype html><html lang="ja"><head><meta charset="utf-8">
<title>第8講 演習問題 解説</title><style>{css}</style></head><body>{body}</body></html>""")
    print("wrote", OUT)


if __name__ == "__main__":
    build()
