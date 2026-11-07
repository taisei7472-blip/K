#!/usr/bin/env python3
"""大問Ⅲ（パルテノン・マーブル）徹底解説 HTML。PDF化: node render.js exam_iii_detail.html ../exam2026_III_detail.pdf"""
import html
import pathlib
import re

from build import annotate_togi

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "exam_iii_detail.html"
E = html.escape


def md(s):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", E(s))


# ---------------------------------------------------------------------------
# 1. なぜ難しいのか：「誰の声か」を見抜く
# ---------------------------------------------------------------------------
VOICES = [
    ("[1]", "But what fun it is to think up smart reasons why this should never happen.", "皮肉",
     "「返さない屁理屈を考えるのは楽しいねえ」。本気で楽しいと言っているのではなく、返還反対派をからかっている。"),
    ("[2]", "Mitsotakis’ reference … might be over the top.", "譲歩",
     "「ギリシャ側も言い過ぎかもね」と一歩譲る → 直後の But から本音（ギリシャ人の恨みは本物）。"),
    ("[3]", "Of course Britain has legal title … / Of course Lord Elgin probably saved them … / Of course repatriating them might be a precedent …", "譲歩×3",
     "返還反対派の言い分を Of course で認めるふり → すべて but / though で否定する。"),
    ("[3]", "It is true that more people see the marbles in London …", "譲歩",
     "It is true that 〜, but … → And so what? で切り捨て。"),
    ("[5]", "It is true that reproduction can nowadays enable …", "譲歩",
     "複製でも美しさは味わえる、と認める → [6] But to the Greeks … authenticity で反論。"),
    ("[7]", "you may have got your independence back, but you are not getting your stuff.", "政府の声（皮肉）",
     "Britain’s government is telling the rest of the world: の後。筆者が英国政府の口ぶりを真似ている。"),
    ("[7]", "You Greeks, it seems to say, were too weak … so that is tough on you.", "政府の声（皮肉）",
     "it seems to say（〜と言っているようだ）が目印。筆者の意見ではない。"),
    ("[7]", "So tell the Greeks they should be proud … They should thank British taxpayers …", "政府の声（皮肉）",
     "命令文・should の連続で、傲慢な口調を誇張して再現している。"),
]

OWN = [
    ("[1]", "The Parthenon marbles row is beyond silly. / Any civilised Briton knows they should be displayed … in their former home of Athens."),
    ("[4]", "The marbles issue is simply about the integrity of one of Europe’s greatest artistic compositions."),
    ("[6]", "surely a cultured country such as Britain should have the dignity to oblige. … Instead it humiliates itself"),
    ("[7]", "a post-imperial arrogance has crept into the marbles debate."),
    ("[8]", "These institutions are fanatically reactionary."),
    ("[9]", "There is nothing sacred about a museum."),
    ("[11]", "most museums have too much stuff, far too much. They should distribute it … Returning the Parthenon marbles might indeed be a precedent, and an excellent one."),
]

# ---------------------------------------------------------------------------
# 2. 語彙（推測のしかたつき）
# ---------------------------------------------------------------------------
VOCAB = [
    ("row", "口論・騒動", "the Parthenon marbles row is beyond silly → 「ばかげた」ものなので騒ぎ。[2] asymmetrical row も同じ。"),
    ("screech", "金切り声をあげる", "“Mine, mine” like a child → 子どもが叫ぶ声。"),
    ("yawn", "あくびをする", "laughs と並ぶ反応。[2] boring と対応 → 退屈。"),
    ("synthetic", "作り物の・わざとらしい", "合成（synthesis）→ 人工的。quest for a daily headline（見出し狙い）からも。"),
    ("over the top", "大げさな・やりすぎの", "top を越える → 度を越している。"),
    ("scholastic", "学者的な・机上の", "school と同語源。boring と並ぶ → 退屈な学問的議論。"),
    ("grievance", "不満・恨み", "grieve（悲しむ）。burning（燃えるような）と組む。"),
    ("asymmetrical", "非対称の", "a（否定）＋symmetrical（対称の）。退屈 ⇔ 恨みの温度差。"),
    ("legal title", "法的所有権", "直後の laws can be changed から「法律上の権利」。"),
    ("repatriate", "本国に返す", "re（戻す）＋patria（祖国）。[10] repatriation も同じ。"),
    ("precedent", "前例", "precede（先に起こる）。"),
    ("integrity", "完全性・一体性", "[3] do not see them complete と対応 → 欠けていないこと。"),
    ("fountainhead", "源泉", "fountain（泉）＋head（源）。"),
    ("cast", "鋳造する", "from bronze と組む → 型に流し込んで作る。cast courts＝石膏像展示室。"),
    ("snobbery", "俗物根性・気取り", "snob。craving for authenticity（本物志向）と結びつく。"),
    ("oblige", "（頼みに）応じる", "have the dignity to oblige → ギリシャの返還要求に応じる。"),
    ("humiliate oneself", "恥をさらす", "humble（低い）と同語源。dignity の反対。"),
    ("take umbrage", "腹を立てる", "over a cup of tea（お茶一杯のことで）→ 子どもっぽい反応。"),
    ("arrogance", "傲慢", "post-imperial arrogance → 帝国時代の名残の思い上がり。"),
    ("inviolability", "不可侵性", "in（否定）＋violate（侵す）＋able。"),
    ("aggrandisement", "権勢の拡大", "grand（大きい）を含む → 国家が大きく見せること。"),
    ("reactionary", "反動的・変化に抵抗する", "react（反発する）→ 新しい流れに逆らう。refusing to dispose と対応。"),
    ("custodian", "管理人・保管者", "custody（保管）。as if … private property of their custodians。"),
    ("in perpetuity", "永久に", "perpetual（永続的な）。locked away と組む。"),
    ("crumble", "崩れる", "walls と組む → 崩れる。if not physically で比喩とわかる。"),
    ("loot", "略奪する", "whether looted or not → 略奪されたかどうか。"),
    ("float", "（案を）出す", "a reform を目的語にとる → 提案する。"),
    ("curb A from doing", "A が〜するのを抑える", "from doing は「妨害・禁止」の型（prevent A from doing と同じ）。"),
]

# ---------------------------------------------------------------------------
# 3. 設問：手順・根拠・全選択肢
# ---------------------------------------------------------------------------
Q = [
    dict(n="1", q="What does the word “screeches” in underline (1) most likely imply?", type="語の含意（下線部）", ans="b",
         steps=["下線を含む文を SVOC で読む：Ⓢ Rishi Sunak Ⓥ screeches Ⓞ “Mine, mine” Ⓜ<like a child in a playground>。",
                "screech を知らなくても、O の “Mine, mine”（ぼくの！ぼくの！）と M の like a child in a playground（遊び場の子どものように）が手がかりになる。",
                "前の文 The Parthenon marbles row is **beyond silly**（ばかげているにもほどがある）から、筆者は首相に否定的。"],
         opts=[("a", "a loud and joyful announcement", "×", "joyful（喜ばしい）が誤り。beyond silly・child から否定的なトーン。"),
               ("b", "a demanding and immature reaction", "○", "“Mine, mine” が demanding（要求がましい）、like a child が immature（未熟な）。"),
               ("c", "a calm and reasoned argument", "×", "calm（冷静）は子どもの叫びと正反対。"),
               ("d", "a political statement of ownership", "×", "**ワナ。** “Mine” から「所有権の主張」を連想させる。だが問われているのは screeches という語が表す「様子・態度」で、like a child が示す子どもっぽさを落としている。")],
         tip="「語の含意」を問う問題は、その語の辞書的な意味だけでなく、同じ文の比喩（like 〜）が示す評価まで答えに入れる。"),
    dict(n="2", q="Blanks [A] and [B] can best be filled by:", type="空所補充（2つ）", ans="d",
         steps=["文の骨格：Ⓢ The nation Ⓥi [A] — Ⓢ polls Ⓥt show Ⓞ[△ over half are [B] to see the marbles returned **and** just above 20% want them to stay]。",
                "まず B から決める（根拠が文中にある方から）。and の前後は対比：「半数以上は返還を見て [B]」⇔「2割強だけが残してほしい」。→ 半数以上は返還に前向き → **happy**。",
                "次に A。直前は He refuses a cup of tea … / The leader of the opposition laughs. と、首相への反応が短文で続く。国民の大半は返還でかまわないので、首相の騒ぎに関心がない → 退屈・無関心。",
                "さらに [2] what to Britain is a **boring** scholastic quarrel（英国にとっては退屈な口論）と対応 → **yawns**（あくびをする）。"],
         opts=[("a", "burps / full", "×", "burp（げっぷ）・full（満腹）。「返還を見て満腹」では意味が通らない。"),
               ("b", "coughs / irritated", "×", "irritated to see the marbles returned（返還を見て苛立つ）が半数以上なら、残してほしい人が多数になり、just above 20% want them to stay と矛盾。"),
               ("c", "snores / despairing", "×", "despairing（絶望して）も b と同じ理由で矛盾。snore（いびき）は「寝ている」で yawn より極端。"),
               ("d", "yawns / happy", "○", "半数以上が返還を喜ぶ → 首相の騒ぎには退屈（yawn）。[2] boring とも一致。")],
         tip="空所が2つある問題は、根拠がはっきりしている方（ここでは B：数字の対比）から決めると選択肢が半分に絞れる。"),
    dict(n="3", q="Blanks [C], [D], and [E] can best be filled by:", type="空所補充（3つ）", ans="d",
         steps=["文の骨格：<as any visitor to [C] knows>, Ⓢ[what to [D] is a boring scholastic quarrel] Ⓥ is Ⓜ to [E] Ⓒ a burning sense of grievance (that will not go away)。",
                "what のカタマリが S（tactics 044）。「D にとっては退屈な学術的口論であるもの」が「E にとっては消えない燃えるような恨み」である、という対比。",
                "恨みを抱くのは奪われた側 → E＝**Greeks**。退屈だと思っているのは持っている側 → D＝**Britain**（[1] The nation yawns とも一致）。",
                "その燃える恨みを「知っている」のは、ギリシャに行ったことのある人 → C＝**Greece**。",
                "直後の This is an **asymmetrical** row（非対称な口論）＝両者の温度差、が確認になる。"],
         opts=[("a", "Britain / Greece / Britons", "×", "恨みを持つのが英国人になり、逆。"),
               ("b", "Britain / Britain / Greeks", "×", "英国を訪れた人がギリシャ人の恨みを知る、は筋が通らない（C が×）。"),
               ("c", "Greece / Greece / Britons", "×", "D・E が逆。ギリシャにとって退屈で、英国人が恨む、になってしまう。"),
               ("d", "Greece / Britain / Greeks", "○", "C 訪問先＝ギリシャ、D 持っている側＝英国、E 奪われた側＝ギリシャ人。")],
         tip="what S is A is B の文は「〜にとって A のものが、…にとって B」という対比文。対比の両側に「誰」が来るかを、文章全体の立場（英国＝持つ側、ギリシャ＝奪われた側）で決める。"),
    dict(n="4", q="What is the author’s attitude towards the argument that more people can see the marbles in London?", type="筆者の態度", ans="c",
         steps=["該当箇所は [3]：It is true that more people see the marbles in London than they would in Athens, **but** they do not see them complete. **And so what?** We are not moving the pyramids to London for a bigger show.",
                "It is true that 〜, but …＝譲歩 → 反論の型。筆者の本音は but の後ろ。",
                "And so what?（それがどうした）＝相手の論点を「関係ない」と切り捨てる表現。",
                "ピラミッドの例：見る人を増やすためにピラミッドをロンドンへ運ばないのと同じで、「見る人の数」は返還しない理由にならない。"],
         opts=[("a", "He almost fully agrees with its logic.", "×", "It is true（確かに）は譲歩にすぎず、すぐ but で否定している。"),
               ("b", "He finds it persuasive but unfortunate.", "×", "persuasive（説得力がある）とは思っていない。And so what? で切り捨てている。"),
               ("c", "He dismisses it as irrelevant or misleading.", "○", "And so what? が dismiss（退ける）、ピラミッドの例で irrelevant（的外れ）。"),
               ("d", "He thinks it proves Britain’s right to keep them.", "×", "筆者は返還派。正反対。")],
         tip="It is true that 〜 / Of course 〜 / might 〜 は譲歩のサイン。筆者の態度は必ず but の後ろで判断する。"),
    dict(n="5", q="What is the author’s view regarding reproduction and authenticity?", type="筆者の見解（複数段落）", ans="b",
         steps=["[5] It is true that reproduction can … enable the naked eye … to appreciate the beauty of the original in a copy.（譲歩：見た目の美しさは複製でも味わえる）",
                "[6] Science could satisfyingly replicate the Parthenon marbles …. **But** to the Greeks … this is indeed about **authenticity**.（反論：ギリシャ人にとっては本物であることが問題）",
                "[6] The Parthenon is their ancestral temple and the marbles their crown jewels.（本物には文化的・象徴的な意味がある）",
                "まとめ：「見て楽しむだけなら複製で十分」＋「でも文化的な意義は本物にしかない」。"],
         opts=[("a", "Reproductions are by definition aesthetically inferior to originals.", "×", "[5] で複製でも美しさは味わえると認めている。aesthetically（美的に）劣るとは言っていない。"),
               ("b", "Reproductions may suffice for visual appreciation but fall short in cultural significance.", "○", "visual appreciation＝[5] appreciate the beauty、cultural significance＝[6] authenticity・ancestral temple。"),
               ("c", "Reproductions could positively contribute to tourism in both London and Athens.", "×", "観光の話は出てこない。in both Athens and London につられないこと。"),
               ("d", "Reproductions have the potential to bring an end to the authenticity debate.", "×", "むしろ「本物かどうか」がギリシャ人にとって核心で、議論は終わらない。")],
         tip="It is true that 〜（[5]）と But（[6]）は段落をまたいでいる。譲歩と反論が離れていても、両方を合わせた選択肢を選ぶ。"),
    dict(n="6", q="Blanks [F] and [G] can best be filled by:", type="空所補充（対比で決める）", ans="a",
         steps=["文：And surely a [F] country such as Britain should have the [G] to oblige. It has the power to restore integrity …. **Instead** it **humiliates itself** by taking umbrage over a cup of tea.",
                "Instead（そうせずに）があるので、「本来すべきこと（G をもって応じる）」⇔「実際にしていること（自ら恥をさらす）」の対比。",
                "humiliate oneself（恥をさらす）の反対 → **dignity**（品位・威厳）。have the dignity to do「品位をもって〜する」は定型。",
                "dignity と相性がよく、筆者が英国に「本来こうあるべき」と期待する国の姿 → **cultured**（教養ある）。[1] Any **civilised** Briton とも対応。"],
         opts=[("a", "cultured / dignity", "○", "humiliates itself との対比で dignity。civilised Briton と cultured country が対応。"),
               ("b", "delicate / prosperity", "×", "have the prosperity to oblige（繁栄をもって応じる）は意味をなさない。"),
               ("c", "prestigious / arrogance", "×", "arrogance（傲慢）は [7] で筆者が批判する態度そのもの。「傲慢さをもって応じるべき」は矛盾。"),
               ("d", "sophisticated / dominance", "×", "have the dominance to oblige は不自然。dominance（支配）も筆者が批判する帝国的な発想。")],
         tip="単語の意味がわからなくても、Instead / but / not 〜 but などの対比の合図があれば、反対側の語から逆算できる（humiliate ⇔ dignity）。"),
    dict(n="7", q="Which of the following is in line with the author’s opinion in paragraph [7]?", type="筆者の意見（皮肉の見抜き）", ans="d",
         steps=["[7] は「筆者の声」と「英国政府の声（皮肉な代弁）」が混ざっている。まず仕分ける。",
                "筆者の声：Bringing empire into these arguments is **rarely helpful**. / But a post-imperial **arrogance** has crept into the marbles debate.",
                "政府の声：Britain’s government is telling the rest of the world: 〜 / You Greeks, **it seems to say**, were too weak … / So tell the Greeks they should be proud … / They should thank British taxpayers …",
                "後半の命令文や should は、政府の傲慢な態度を誇張して真似したもの（皮肉）。筆者がそう思っているのではない。",
                "筆者の意見は arrogance への批判 →「英国政府は尊大な態度を恥じるべき」。"],
         opts=[("a", "The history of imperialism can be valid evidence in favour of Britain’s right to keep the marbles.", "×", "筆者は Bringing empire into these arguments is rarely helpful と言っている。"),
               ("b", "The Greeks cannot blame Britain because their ancestors were not strong enough to protect their marbles.", "×", "**ワナ。** You Greeks … were too weak to stop the Ottomans の言い換えだが、これは it seems to say がついた政府の声。"),
               ("c", "Greece must be content with the fact that their marbles are exhibited in the British Museum with other masterpieces from around the world.", "×", "**ワナ。** So tell the Greeks they should be proud to see their relics sit alongside the finest of Africa and Asia の言い換え。これも皮肉な代弁。"),
               ("d", "The British government should be ashamed of its self-important attitude with regard to other cultures’ artefacts.", "○", "self-important attitude＝arrogance。ashamed は [6] humiliates itself とも対応。")],
         tip="本文の言い換えになっている選択肢でも、それが「誰の声」かを確認する。telling 〜: / it seems to say / 命令文の連続は、筆者が他人の主張を真似している合図。"),
    dict(n="8", q="According to the author, what is the core difference between Greek and British views of the marbles?", type="対比の整理", ans="b",
         steps=["ギリシャ側：[6] this is indeed about **authenticity** / The Parthenon is their **ancestral temple** and the marbles their **crown jewels** / They badly want them back.",
                "英国側：[3] more people see the marbles in London / a bigger **show** / [7] they should be proud to see their relics **sit alongside** the finest of Africa and Asia（並べて展示）。",
                "まとめ：ギリシャ＝祖先の神殿・至宝（象徴的な遺産）、英国＝人に見せる展示品。"],
         opts=[("a", "The Greeks want financial compensation; the British do not.", "×", "金銭的補償の話は本文にない。"),
               ("b", "The Greeks see them as symbolic heritage; the British as display items.", "○", "ancestral temple・crown jewels＝symbolic heritage、show・more people see＝display items。"),
               ("c", "The Greeks believe they are Ottoman property; the British disagree.", "×", "オスマン人は手放した側として出てくるだけ。所有者だとは言っていない。"),
               ("d", "The Greeks think replicas are unacceptable; the British don’t want any.", "×", "英国が複製を望まない、とは書かれていない。前半も「複製は受け入れられない」とまでは言っていない。")],
         tip="「核心の違い」を問う問題は、両者それぞれの表現を本文から集めて、抽象度を一段上げた言葉（symbolic heritage / display items）に置き換えて照合する。"),
    dict(n="9", q="How does the author characterise the British Museum?", type="筆者の評価", ans="c",
         steps=["[8] These institutions are **fanatically reactionary**.（狂信的に反動的）",
                "[8] They want to **deny** newly emergent countries the scope to acquire similar collections by **refusing to dispose** … their vast reserves.（手放さない・他国に与えない）",
                "[8] Many have the vast amount of their works in store, **as if they were the private property of their custodians**.（まるで私物のように）",
                "[9] It is an unnatural place to leave thousands of objects frozen …（不自然な保管場所）",
                "→ 他文化の財産を抱え込んで手放さない、貪欲な保管者。"],
         opts=[("a", "as a benevolent guardian of world heritage", "×", "benevolent（慈悲深い）は正反対。inviolability や global context は政府側の言い分として皮肉で出てくるだけ。"),
               ("b", "as a dynamic institution eager to modernise", "×", "reactionary（変化に抵抗する）と正反対。"),
               ("c", "as a greedy keeper of other cultures’ property", "○", "refusing to dispose・as if … private property が greedy keeper。"),
               ("d", "as a neutral institution committed to scholarly access", "×", "**ワナ。** [8] declared itself primarily a research resource for scholars を使った選択肢。だが even（〜さえ）がついていて、公開せず学者向けに囲い込む態度を批判する文脈。neutral（中立）でもない。")],
         tip="本文の語句をそのまま使った選択肢（d の scholars）は、本文での評価（プラスかマイナスか）まで一致しているか確認する。even は「そこまでするか」という筆者の批判の合図。"),
    dict(n="10", q="Why does the author think the arguments for keeping the marbles are flawed?", type="理由（消去法）", ans="c",
         steps=["「保持する側の議論」は [3] にまとめて出てくる。筆者は Of course 〜, but … でそれぞれに反論している。",
                "① legal title（法的所有権）→ but laws can be changed",
                "② Elgin saved them → though they were later damaged",
                "③ might be a precedent → but not if you don’t（前例にしたくなければならない）",
                "④ more people see them → but they do not see them complete. And so what?",
                "選択肢の中で、この反論と一致するのは「法的な形式論にもとづいている」だけ。筆者が最初に挙げ、[11] で法改正（reform of the National Heritage Act）の話で締めくくる中心の論点でもある。"],
         opts=[("a", "The British Museum does not have proper facilities.", "×", "**ワナ。** [9] vulnerable to theft and decay は博物館一般が「不自然な場所」だという話で、大英博物館の設備不足を保持論の欠陥として挙げてはいない。"),
               ("b", "British citizens overwhelmingly support keeping them.", "×", "[1] の世論調査では返還賛成が半数以上。正反対。"),
               ("c", "The arguments are based on legal technicalities.", "○", "legal title に対して laws can be changed。法律上の権利は変えられる形式にすぎない、という反論。"),
               ("d", "They have already been returned without public notice.", "×", "返還されたという事実はない。")],
         tip="「なぜ〜は誤りだと考えるか」は、本文で筆者が反論している箇所（but の後ろ）を集め、選択肢と1つずつ照合する消去法が確実。"),
    dict(n="11", q="What does the author mean by underline (2)?", type="下線部の意味（比喩）", ans="b",
         steps=["Ⓢ Museum walls Ⓥi are now crumbling Ⓜ ideologically Ⓜ<if not physically>.",
                "**if not 〜「たとえ〜でないにしても／〜とまではいかなくても」**（tactics 093：if＋語）。例：difficult, if not impossible「不可能とまではいかなくても難しい」。",
                "→「物理的にではないにしても、思想的には崩れつつある」。壁が崩れるのは比喩で、博物館を支えてきた考え方が崩れている、という意味。",
                "直後の具体例：France has a major programme of repatriation … So does Germany. … African bronzes are returning to Africa … → 返還の流れ＝「返さない」という従来の理屈が通用しなくなっている。"],
         opts=[("a", "Museums are physically deteriorating due to poor maintenance.", "×", "if not physically を「物理的に」と読み違えたワナ。"),
               ("b", "Traditional justifications for museum practices are losing ground.", "○", "ideologically crumbling＝考え方（正当化の理屈）が崩れる＝losing ground（力を失う）。"),
               ("c", "Museums are being relocated to digital environments.", "×", "デジタル化の話はない。"),
               ("d", "Visitors have been vandalising museum walls during protests.", "×", "物理的な破壊なので不可。")],
         tip="A if not B は「B ではないにしても A」。B の方を否定しているので、if not の後ろの語（physically）を答えに選ばないこと。"),
    dict(n="12", q="Which of the following statements is NOT in line with the content of the article?", type="内容不一致（NOT）", ans="b",
         steps=["NOT 問題は、一致する3つを根拠つきで消し、残った1つを確認する。",
                "a：[3] Of course Britain has **legal title** to the statues → 法的には英国のもの。一致。",
                "c：[9] vulnerable to **theft and decay** → 盗難や劣化の危険。一致。",
                "d：[10] France has a major programme of **repatriation** of imperial objects → 一致。",
                "b：[10] This does **not** mean the death of the Louvre（ルーヴルが終わるわけではない）と言っているだけ。「最も重要な品をルーヴルに集めるべき」とは言っていない。むしろ筆者は分散・返還を主張（[11] distribute it to the rest of the world）。"],
         opts=[("a", "Legally, the marbles belong to Britain rather than to Greece.", "一致", "[3] legal title。筆者は「法律は変えられる」と言うが、現在の法的所有が英国にあることは認めている。"),
               ("b", "The most important objects of antiquity should be concentrated at the Louvre.", "○（不一致）", "[10] はルーヴルが存続するというだけ。集中ではなく分散が筆者の主張。"),
               ("c", "Objects stored in museums could wear out or be stolen.", "一致", "[9] vulnerable to theft and decay。wear out＝decay。"),
               ("d", "France has begun returning objects it previously collected to their countries of origin.", "一致", "[10] France has a major programme of repatriation。")],
         tip="筆者が反対している事実（法的所有権が英国にあること）も「本文の内容」としては一致になる。NOT 問題では「筆者が賛成か」ではなく「本文に書いてあるか」で判断する。"),
    dict(n="13", q="Which of the following titles best matches the content of the article?", type="タイトル選択", ans="a",
         steps=["タイトルは「主張（筆者の結論）」と「話題」の両方を含むものを選ぶ。",
                "話題：パルテノン・マーブルの返還問題。筆者の立場：返還すべき（[1] they should be displayed … in Athens）。",
                "結論：[11] The truth is that most museums have **too much stuff**, far too much. … Returning the Parthenon marbles might indeed be a precedent, and an excellent one."],
         opts=[("a", "Return the Parthenon marbles: The British Museum has too much stuff anyway", "○", "前半＝筆者の主張、後半＝[11] too much stuff。主張と根拠の両方を含む。"),
               ("b", "Marvelous marbles from Greece: Let’s leave them in London", "×", "主張が正反対。"),
               ("c", "How they lost their marbles: Debating Greece’s claims to the Parthenon sculptures", "×", "lose one’s marbles（正気を失う）のしゃれ。Debating（議論の紹介）では中立的すぎて、返還を強く主張する筆者の立場が出ていない。"),
               ("d", "From Athens to London and back again: The long journey of the Parthenon marbles", "×", "マーブルの移動の歴史が中心の話ではない。and back again（返還済み）も事実と違う。")],
         tip="タイトル問題は、①話題が合っているか、②筆者の立場（賛成・反対）が合っているか、③範囲が広すぎ・狭すぎないか、の順にチェックする。"),
]

ANNOT = [
    ("[1]", "{S|The nation} {Vi|[ A ]} — {S|polls} {Vt|show} {O|[△ {S'|over half} {V'|are} {C'|[ B ]} {M'|<to see the marbles returned>} and {S'|just above 20%} {V't|want} {O'|them} {C'|to stay}]}."),
    ("[2]", "But {M|<as any visitor (to [ C ]) knows>}, {S|[what ⟪S'欠⟫ {M'|to [ D ]} {V'|is} {C'|a boring scholastic quarrel}]} {V|is} {M|to [ E ]} {C|a burning sense of grievance (that ⟪S'欠⟫ will not go away)}."),
    ("[3]", "{S|It} {V|is} {C|true} {S|[that {S'|more people} {V't|see} {O'|the marbles} {M'|in London} {M'|<than they would △ in Athens>}]}, but {S|they} {Vt|do not see} {O|them} {C|complete}. And so what?"),
    ("[6]", "And {M|surely} {S|a [ F ] country (such as Britain)} {Vt|should have} {O|the [ G ] (to oblige)}. … {M|Instead} {S|it} {Vt|humiliates} {O|itself} {M|<by taking umbrage over a cup of tea>}."),
    ("[10]", "{S|Museum walls} {Vi|are now crumbling} {M|ideologically} {M|<if not physically>}."),
]

CSS_EXTRA = """
table.t { width:100%; border-collapse:collapse; font-size:9.4pt; margin-bottom:3mm; }
.t td, .t th { border:1px solid #999; padding:1mm 2mm; vertical-align:top; }
.t th { background:var(--soft); }
.t td.k { white-space:nowrap; font-weight:bold; width:12mm; text-align:center; }
.t td.e { font-family:"Liberation Serif",serif; }
.t td.tag { width:20mm; font-weight:bold; }
.voice-irony { color:#b3261e; } .voice-own { color:#15803d; }
.qbox { border:1.5px solid var(--ink); padding:3mm 4mm; margin:0 0 4mm; break-inside:avoid-page; }
.qbox .qq { font-family:"Liberation Serif",serif; font-size:11pt; margin:1mm 0 2mm; }
.qbox .meta { font-size:9pt; color:#555; }
.qbox .ans { display:inline-block; background:#fff1a6; border:1px solid #111; padding:0 2.5mm; font-weight:bold; margin-left:2mm; }
.qbox ol { margin:1mm 0 2mm; padding-left:1.4em; font-size:9.8pt; line-height:1.75; }
.opts td.v { width:16mm; text-align:center; font-weight:bold; white-space:nowrap; }
.opts tr.ok td { background:#fff8cc; }
.tipq { border-left:4px solid #15803d; background:#eef8ec; padding:1.5mm 3mm; font-size:9.6pt; }
.intro { border:2px solid var(--ink); padding:3mm 4mm; margin-bottom:4mm; line-height:1.85; font-size:10pt; }
"""


def build():
    css = (HERE / "style.css").read_text() + CSS_EXTRA
    voices = "".join(f'<tr><td class="k">{E(p)}</td><td class="e">{E(s)}</td><td class="tag voice-irony">{E(t)}</td><td>{E(x)}</td></tr>'
                     for p, s, t, x in VOICES)
    own = "".join(f'<tr><td class="k">{E(p)}</td><td class="e voice-own">{E(s)}</td></tr>' for p, s in OWN)
    vocab = "".join(f'<tr><td class="e"><b>{E(w)}</b></td><td>{E(j)}</td><td>{E(h)}</td></tr>' for w, j, h in VOCAB)
    ann = "".join(f'<div class="sent"><div class="pattern">{E(p)}</div><div class="en togi">{annotate_togi(a)}</div></div>' for p, a in ANNOT)
    qs = []
    for q in Q:
        steps = "".join(f"<li>{md(s)}</li>" for s in q["steps"])
        opts = "".join(f'<tr class="{"ok" if v.startswith("○") else ""}"><td class="k">{E(l)}</td><td class="e">{E(t)}</td><td class="v">{E(v)}</td><td>{md(r)}</td></tr>'
                       for l, t, v, r in q["opts"])
        qs.append(f"""
<div class="qbox">
  <div class="meta">問{q['n']}　【{E(q['type'])}】<span class="ans">正解 {E(q['ans'])}</span></div>
  <div class="qq">{E(q['q'])}</div>
  <b>解く手順</b>
  <ol>{steps}</ol>
  <b>選択肢の検討</b>
  <table class="t opts">{opts}</table>
  <div class="tipq">▶ {E(q['tip'])}</div>
</div>""")
    demo = annotate_togi("{S|S} {Vt|V} {O|O} {M|M}")
    body = f"""
<div class="cover">
  <div class="kicker">2026年度 英語　大問Ⅲ 徹底解説</div>
  <h1>パルテノン・マーブル論争 <small>— 皮肉と譲歩を見抜いて解く</small></h1>
</div>
<div class="intro"><b>この大問が難しい理由</b><br>
この文章は返還を主張するコラムだが、筆者は自分の意見をストレートに言うだけでなく、<b>①反対派の言い分をいったん認める（譲歩）</b>、<b>②英国政府の口ぶりを真似てからかう（皮肉）</b>、という書き方を何度も使う。
そのため、本文の言い換えになっている選択肢でも、それが「筆者の声」ではなく「他人の声」なら不正解になる（問4・5・7・9・10）。
まず「筆者はギリシャへの返還に賛成」という立場を [1] で確定し、各文が「筆者の声」か「譲歩・皮肉」かを仕分けながら読むのがコツ。</div>

<h2><span class="num">1</span>「誰の声か」を仕分ける</h2>
<h3>筆者の声ではない文（譲歩・皮肉）</h3>
<table class="t"><tr><th>段落</th><th>本文</th><th>種類</th><th>読み方</th></tr>{voices}</table>
<h3>筆者自身の主張（ここだけ拾えば立場がわかる）</h3>
<table class="t"><tr><th>段落</th><th>本文</th></tr>{own}</table>

<section class="sec page">
<h2><span class="num">2</span>設問に直結する文の構造</h2>
<div class="legend togi"><div>{demo}　黄色＝S・V・O・C、緑＝M。△＝省略、<span class="gap">●</span>＝欠けている位置</div></div>
{ann}
<h3>語彙（推測のしかたつき）</h3>
<table class="t"><tr><th>語句</th><th>意味</th><th>知らなくても推測できる手がかり</th></tr>{vocab}</table>
</section>

<section class="sec page">
<h2><span class="num">3</span>設問の徹底解説</h2>
{''.join(qs)}
</section>

<section class="sec page">
<h2><span class="num">4</span>大問Ⅲで使った解き方のまとめ</h2>
<ul class="points">
  <li><b>筆者の立場を最初に確定する</b>：[1] beyond silly／Any civilised Briton knows they should be displayed … in Athens → 返還賛成。これと逆の選択肢はほぼすべて消える（問2 b・c、問4 d、問7 a・b・c、問9 a、問13 b）。</li>
  <li><b>譲歩のサイン</b>（Of course／It is true that／might be over the top）の後は必ず but・though・And so what? で反論が来る。筆者の意見は反論の側（問4・5・10）。</li>
  <li><b>皮肉・代弁のサイン</b>（is telling 〜:／it seems to say／命令文・should の連続）がある文は筆者の意見ではない（問7）。</li>
  <li><b>対比の合図</b>（Instead／but／⇔ の形容詞）があれば、知らない語でも反対側の語から逆算できる（問3 boring ⇔ burning、問6 humiliate ⇔ dignity）。</li>
  <li><b>if not B</b> は「B ではないにしても」。B は否定されている側（問11）。</li>
  <li><b>本文の語句をそのまま使った選択肢</b>は、本文でのプラス・マイナスの評価まで一致しているか確認する（問1 d、問7 b・c、問9 d）。</li>
</ul>
</section>
"""
    OUT.write_text(f"""<!doctype html><html lang="ja"><head><meta charset="utf-8">
<title>大問Ⅲ 徹底解説</title><style>{css}</style></head><body>{body}</body></html>""")
    print("wrote", OUT)


if __name__ == "__main__":
    build()
