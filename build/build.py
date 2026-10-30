#!/usr/bin/env python3
"""英語長文 V の解答・解説 HTML を生成する。PDF化は render.js で行う。"""
import html
import pathlib
import re

from syntax import TOGI

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "passage_v.html"

# ---------------------------------------------------------------------------
# 本文データ
#   annotated: 文構造用のマークアップ
#     {L|...}  L = ラベル。S V O C 真S 強調 は主節、末尾に ' が付くと従属節
#     ( )  形容詞的なカタマリ   [ ]  名詞的なカタマリ   ⟨ ⟩  副詞的なカタマリ
#   notes: 構文メモ  /  ja: 和訳
# ---------------------------------------------------------------------------
PARAS = [
    ("A", [
        dict(
            annotated="{S|The search for the identity of a nation} almost always {V|emerges} ⟨as a reaction to a challenge to pre-existing assumptions (caused by an encounter with an alien existence)⟩.",
            notes=["as a reaction to 〜「〜に対する反応として」。as は前置詞。",
                   "caused by 〜 は過去分詞の後置修飾。意味上は a challenge を修飾（「異質な存在との遭遇によって引き起こされた挑戦」）。",
                   "a challenge to 〜「〜への異議・挑戦」。to は前置詞。"],
            ja="国家のアイデンティティの探求は、ほとんど常に、異質な存在との遭遇によって引き起こされた、既存の前提への挑戦に対する反応として現れる。"),
        dict(
            annotated="⟨At such times⟩, {S|the history of the nation} {V|is invented} ⟨as a storehouse of knowledge (from which {S'|the inventor} ⟨as a member of the nation⟩ {V'|can draw} {O'|guides of behaviour})⟩.",
            notes=["from which は「前置詞＋関係代名詞」。先行詞は a storehouse of knowledge。draw A from B「B から A を引き出す」の from B が前に出た形。",
                   "as a member of the nation は挿入された副詞句。S' と V' の間に入っている。"],
            ja="そのような時、国家の歴史は、国家の一員である創作者が行動の指針を引き出せる知識の貯蔵庫として創り出される。"),
        dict(
            annotated="{S|The origin of the nation} especially {V|is} {C|a convenient object for this creative activity} ⟨because {S'|it} {V'|belongs} to the prehistoric era (for which {S'|conclusive historical material} {V'|is} {C'|extremely rare} ⟨compared to other historical times⟩)⟩.",
            notes=["this creative activity は前文の「歴史を創作すること」を指す。",
                   "for which の先行詞は the prehistoric era。material is rare for the era「その時代については資料が乏しい」。",
                   "compared to 〜「〜と比べて」は分詞構文由来の慣用表現。"],
            ja="とりわけ国家の起源は、この創造的な活動にとって都合のよい対象である。なぜなら起源は、他の歴史上の時代と比べて決定的な歴史資料がきわめて乏しい先史時代に属しているからである。"),
    ]),
    ("B", [
        dict(
            annotated="{S|No consensus} {V|exists} ⟨as to the theory of the origin of the Japanese nation⟩.",
            notes=["as to 〜「〜に関して」。No consensus exists は「合意は存在しない」（第1文型）。"],
            ja="日本民族の起源に関する説については、合意が存在しない。"),
        dict(
            annotated="⟨Just like constellations (formed ⟨by drawing lines between stars⟩)⟩, {S|different individuals} {V|form} {O|different theories} ⟨by combining scraps of historical materials⟩.",
            notes=["Just like 〜「ちょうど〜のように」。formed 以下は constellations を後ろから修飾する過去分詞句。",
                   "by drawing / by combining の by ＋動名詞は「〜することによって」。星をつないで星座を作るのと、資料の断片をつないで説を作ることが対応する比喩。"],
            ja="星と星の間に線を引くことで星座が形づくられるのとちょうど同じように、人はそれぞれ歴史資料の断片を組み合わせて、別々の説を作り上げる。"),
        dict(
            annotated="However, {S|the theory of the Japanese nation} {V|altered} ⟨whenever {S'|Japanese relations with the outside world} {V'|changed}⟩.",
            notes=["whenever「〜するときはいつでも」。副詞節を導く。alter はここでは自動詞「変わる」。"],
            ja="しかし、日本民族に関する説は、日本と外の世界との関係が変わるたびに変化してきた。"),
        dict(
            annotated="⟨In talking about the history of the Japanese nation⟩, {S|many theorists} merely {V|express} {O|[what {V'|is taking place} ⟨in their own subconscious⟩]}.",
            notes=["in ～ing「〜するときに」。",
                   "what は関係代名詞（＝the thing which）で、名詞節の中では S' のはたらき。merely「〜にすぎない」。"],
            ja="日本民族の歴史を語るとき、多くの論者は、自分自身の潜在意識の中で起きていることを表しているにすぎない。"),
    ]),
    ("C", [
        dict(
            annotated="⟨For mankind⟩, {S|nothing} {V|is} {C|more attractive} ⟨than the ability (to talk freely about one's past)⟩.",
            notes=["否定主語＋比較級＋than ～ で最上級の意味：「〜ほど魅力的なものはない」。",
                   "to talk は the ability を修飾する形容詞的用法の不定詞。"],
            ja="人類にとって、自分の過去を自由に語れることほど魅力的なものはない。"),
        dict(
            annotated="{S|One} {V|might be} {C|the descendant of any of the following}: a pure and unstained nation, a fearless horse-riding group (which {V'|conquered} {O'|an indigenous people}), a middle-eastern nation (depicted in the Bible), a farming nation (that {V'|migrated} ⟨from the south islands⟩).",
            notes=["コロン以下の4つの名詞句は the following の具体的な中身（同格）。",
                   "which / that は主格の関係代名詞で、関係詞節内の S' にあたる。depicted は過去分詞の後置修飾。",
                   "4つの例は、単一民族説、騎馬民族征服説、日ユ同祖論、南方起源説という日本人起源論の代表例を指す。"],
            ja="人は、次のどれの子孫でもありうる。純粋で汚れのない民族、先住民を征服した勇猛な騎馬民族、聖書に描かれた中東の民族、南の島々から移り住んだ農耕民族。"),
        dict(
            annotated="Perhaps, {S|the reason (why {S'|the theory of the origin of the Japanese nation} {V'|has been and remains} {C'|so popular} ⟨in Japan⟩)} {V|is} {C|[that {S'|it} {V'|is} {C'|the best way (for people to live their dreams)}]}.",
            notes=["The reason why S' V' is that ～「S' が V' する理由は〜だ」。why は関係副詞。",
                   "has been and remains so popular は「これまで人気があったし今も人気がある」。2つの動詞が補語 so popular を共有している。",
                   "for people は不定詞 to live の意味上の主語。"],
            ja="おそらく、日本民族の起源論が日本でこれまでも、そして今も、これほど人気があるのは、それが人々にとって夢を生きる最良の方法だからであろう。"),
    ]),
    ("D", [
        dict(
            annotated="⟨Even today⟩, {S|many people} {V|discuss} {O|the character of the “Japanese,”} and {V|develop} {O|arguments on modern Japanese society}, ⟨based on their ideas of the origin of the nation⟩.",
            notes=["discuss と develop の2つの V が and で並列。共通の S は many people。",
                   "based on 〜「〜に基づいて」は過去分詞から来た副詞句。"],
            ja="今日でさえ、多くの人々が「日本人」の性格を論じ、民族の起源についての自分の考えに基づいて、現代日本社会についての議論を展開している。"),
        dict(
            annotated="{C|What sort of relationship}, however, {V|is} there ⟨between a time ⟨thousands or tens of thousands of years ago⟩ (when, ⟨it is presumed⟩, {S'|the nation} {V'|originated}), and the politics and society of today⟩?",
            notes=["There is 構文の疑問文。S は What sort of relationship（ラベルは S）。between A and B の A＝a time … originated、B＝the politics and society of today。",
                   "when は関係副詞で、先行詞は a time。it is presumed「〜と推定されている」は挿入。",
                   "「どんな関係があるというのか」→「ほとんど関係はない」という修辞疑問。"],
            ja="しかし、民族が誕生したと推定される数千年あるいは数万年前の時代と、今日の政治や社会との間に、いったいどのような関係があるというのだろうか。"),
        dict(
            annotated="{S|The only link between the two} {V|is} {C|the tacit premise} both [that {S'|the inhabitants of the archipelago ⟨thousands of years ago⟩} {V'|were} already {C'|“Japanese,”}] and [that {S'|their character} {V'|has remained} {C'|unchanged} ⟨ever since⟩].",
            notes=["both [that ～] and [that ～] の2つの that 節は the tacit premise の内容を表す同格節。",
                   "remain＋C「C のままである」。ever since「それ以来ずっと」。",
                   "the two＝前文の「数千年前の時代」と「今日の政治・社会」。"],
            ja="両者を結ぶ唯一のつながりは、数千年前の列島の住民がすでに「日本人」であったことと、彼らの性格がそれ以来ずっと変わっていないことの両方を暗黙の前提にすることだけである。"),
    ]),
    ("E", [
        dict(
            annotated="⟨Even if {S'|today's Japan} {V'|is} {C'|relatively homogeneous} ⟨compared to other countries⟩⟩, {S|the main reason for this} {V|lies} ⟨in the international conditions of the nineteenth century (that {V'|allowed} {O'|Japan} {C'|to avoid being colonized} but {V'|did not enable} {O'|it} {C'|to become advanced enough to establish a large-scale empire})⟩.",
            notes=["【空所50】conditions：international conditions「国際的な情勢・条件」。",
                   "lie in 〜「〜にある」。that は主格の関係代名詞で、先行詞は the international conditions。",
                   "allow O to do / enable O to do「O が〜するのを可能にする」。O と to 不定詞の間に主述関係があるので、O'・C' として扱う。",
                   "avoid being colonized：avoid の後ろは動名詞で、ここでは受動態の being＋過去分詞。",
                   "形容詞＋enough to do「〜できるほど…」。"],
            ja="たとえ今日の日本が他国に比べて比較的均質だとしても、その主な理由は19世紀の国際的な条件にある。その条件は、日本が植民地化されるのを避けることは可能にしたが、大規模な帝国を築けるほど先進的になることは可能にしなかった。"),
        dict(
            annotated="⟨Unlike many third-world countries⟩, {S|Japan} {V|did not experience} {O|a colonial rule (under which {S'|borders} {V'|were drawn up} ⟨despite traditional ethnic boundaries⟩) or a policy of rule through division (that {V'|intensified} {O'|differences between ethnic groups})}, nor {V|were} {S|large numbers of alien peoples from other continents} {V|introduced} ⟨to provide labour⟩.",
            notes=["【空所51】rule：colonial rule「植民地支配」。under which で「その支配の下で」とつながる。",
                   "【空所52】boundaries：traditional ethnic boundaries「伝統的な民族の境界」。borders（国境）との対比。",
                   "【空所53】labour：to provide labour「労働力を供給するために」。目的を表す不定詞の副詞的用法。",
                   "nor＋倒置：nor were S introduced「S が持ち込まれることもなかった」。否定の接続詞 nor の後ろは疑問文の語順になる。",
                   "a policy of rule through division は「分割による統治の政策」（＝分割統治 divide and rule）。"],
            ja="多くの第三世界の国々とは違い、日本は、伝統的な民族の境界を無視して国境線が引かれるような植民地支配も、民族集団間の違いを強めるような分割統治政策も経験しなかった。また、労働力を供給するために他の大陸から大量の異民族が連れてこられることもなかった。"),
    ]),
    ("F", [
        dict(
            annotated="Furthermore, ⟨unlike many other imperial powers⟩, {S|Japan} {V|did not advance} ⟨into remote regions⟩.",
            notes=["【並べ替え ii】Furthermore「さらに」は、[E] の「日本が経験しなかったこと」に追加する合図。"],
            ja="さらに、他の多くの帝国主義国と違って、日本は遠く離れた地域には進出しなかった。"),
        dict(
            annotated="Nor {V|did} {S|she} {V|rule} {O|her colonies} ⟨long enough to establish a close relationship (that {V'|would allow for} {O'|large-scale migration} ⟨even after {S'|her former colonies} {V'|became} {C'|independent}⟩)⟩ ⟨as happened in the case of Great Britain⟩.",
            notes=["【並べ替え iv】Nor＋倒置（did she rule）。直前の否定文（ii の did not advance）を受けて「〜もしなかった」。",
                   "she＝Japan。国家を女性代名詞で受ける古い用法。",
                   "allow for 〜「〜を可能にする」。",
                   "as happened in 〜 の as は関係代名詞的に使われ、「〜で起きたように」。as の指す内容は「旧植民地との緊密な関係から大規模な移住が起きたこと」。"],
            ja="また、イギリスの場合に起きたように、旧植民地が独立した後でさえ大規模な移住を可能にする緊密な関係を築けるほど長く、植民地を支配することもなかった。"),
        dict(
            annotated="⟨If {S'|Japan} {V'|had been divided and ruled} ⟨in the nineteenth century⟩⟩, {S|“Japanese” (living in the south of Japan)} {V|might have been classified} ⟨as a different ethnic group with a different language from those (living in the north)⟩.",
            notes=["【並べ替え iii】仮定法過去完了：If S had p.p., S might have p.p.「もし〜だったら、…だったかもしれない」。",
                   "divided and ruled は、[E] の a policy of rule through division（分割統治）を言い換えたもの。",
                   "different A from B「B とは異なる A」。those＝the “Japanese”。living は現在分詞の後置修飾。"],
            ja="もし日本が19世紀に分割統治されていたら、日本の南部に住む「日本人」は、北部に住む人々とは異なる言語をもつ別の民族集団に分類されていたかもしれない。"),
        dict(
            annotated="There {V|might even have been} {S|an established anthropological theory (supporting the differences between the two)}.",
            notes=["【並べ替え i】There＋V＋S の構文（There は誘導副詞なので S ではない）。might have been も仮定法過去完了の帰結。",
                   "the two＝iii の「南部の日本人」と「北部の人々」。だから iii → i の順になる。"],
            ja="両者の違いを裏づける、確立した人類学の理論さえ存在していたかもしれない。"),
    ]),
    ("G", [
        dict(
            annotated="{S|Not only Japan but almost all nation-states} {V|have created} {O|myths about their origins}.",
            notes=["not only A but (also) B「A だけでなく B も」。動詞は B（almost all nation-states）に一致するので have。"],
            ja="日本だけでなく、ほとんどすべての国民国家が、自らの起源についての神話を作り上げてきた。"),
        dict(
            annotated="⟨Unlike the heroism of many myths⟩, however, {S|[what {V'|lies} ⟨behind this way of thinking (that {V'|searches for} {O'|myths})⟩]} {V|is} {C|the desire (to escape present realities)}.",
            notes=["what は関係代名詞で、what 節全体が文の S。",
                   "that は主格の関係代名詞で、先行詞は this way of thinking。",
                   "to escape は the desire の内容を表す不定詞（形容詞的用法）。"],
            ja="しかし、多くの神話がもつ英雄的な性格とは裏腹に、神話を探し求めるこうした考え方の背後にあるのは、目の前の現実から逃れたいという願望である。"),
    ]),
    ("H", [
        dict(
            annotated="{S|The essence of mythologizing the past} {V|is} {C|to escape from the trouble and fear (involved in facing up to the Other)}, and {C|to project onto the past categories (that {S'|people} {V'|wish to apply} ⟨to the present⟩)}.",
            notes=["補語は2つの不定詞（to escape ～ と to project ～）が and で並列している。",
                   "project A onto B「A を B に投影する」。目的語 A（categories ～）が長いので後ろに回り、project onto the past categories … の語順になっている。",
                   "that は目的格の関係代名詞（apply の目的語）。apply A to B「A を B に当てはめる」。",
                   "the Other「他者」。大文字で、自分とは異質な存在全般を表す。"],
            ja="過去を神話化することの本質は、他者と向き合うことに伴う面倒や恐怖から逃れることであり、人々が現在に当てはめたいと望む分類を過去に投影することである。"),
        dict(
            annotated="Of course, {S|stereotypes} {V|are} ⟨to some degree⟩ {C|necessary} ⟨for human life⟩.",
            notes=["Of course ～. However, ～.「もちろん〜だ。しかし〜」という譲歩→主張の型。"],
            ja="もちろん、ステレオタイプはある程度は人間の生活に必要である。"),
        dict(
            annotated="However, {S|to avoid directly confronting the Other, and gradually to create stereotypes, to escape into myths, and to attempt to explain the entire world with a single story ⟨because {S'|we} {V'|are not able to endure} {O'|the shock of even a small-scale interaction}⟩}, {V|is} {C|to deny and oppress the Other}.",
            notes=["【空所X】attempt to explain the entire world with a single story。5番目は entire、9番目は single。",
                   "S は4つの不定詞句（to avoid / to create / to escape / to attempt）の並列で、全体を1つの行為とみなすので V は単数の is。",
                   "because 節は S の中にあり、4つの行為をする理由を述べる。",
                   "avoid＋動名詞（confronting）。even a small-scale interaction「ほんの小さな交流でさえ」。"],
            ja="しかし、ほんの小さな交流の衝撃にさえ耐えられないからといって、他者と直接向き合うのを避け、少しずつステレオタイプを作り、神話に逃げ込み、たった一つの物語で世界全体を説明しようとすることは、他者を否定し抑圧することである。"),
        dict(
            annotated="⟨Here⟩ {V|lies} {S|the origin of all myths}.",
            notes=["場所の副詞 Here が文頭に出て、V＋S の倒置が起きている（＝The origin of all myths lies here.）。"],
            ja="ここにこそ、あらゆる神話の起源がある。"),
    ]),
    ("I", [
        dict(
            annotated="{S|The conclusion}, therefore, {V|is} {C|very simple}.",
            notes=["therefore は挿入。前の議論からの結論を示す合図。"],
            ja="したがって、結論はきわめて単純である。"),
        dict(
            annotated="{S|It} {V|is} not {C|sufficient} {真S|to fight against myths ⟨by destroying one myth and replacing it with another⟩}, ⟨as in, for example, criticising the myth of the homogeneous nation and substituting it with the myth of the mixed nation⟩.",
            notes=["It は形式主語で、真主語は to fight ～。",
                   "【空所(a)】criticising：as in ～ing「〜する場合のように」。in の後ろなので動名詞になり、substituting と並列する。",
                   "replace A with B / substitute A with B「A を B に置き換える」。"],
            ja="たとえば単一民族の神話を批判し、それを混合民族の神話に置き換える場合のように、ある神話を壊して別の神話に置き換えることで神話と戦うだけでは十分ではない。"),
        dict(
            annotated="Instead, ultimately {S|we} {V|should aim} {O|to liberate ourselves from all myths}.",
            notes=["aim to do「〜することを目指す」。liberate oneself from 〜「〜から自分を解放する」。"],
            ja="そうではなく、究極的には、私たちはあらゆる神話から自分を解放することを目指すべきである。"),
        dict(
            annotated="{S|This} {V|is} {C|something (which {V'|will require} {O'|some work})}.",
            notes=["which は主格の関係代名詞。some work「それなりの努力」。"],
            ja="これは、ある程度の努力を必要とすることである。"),
        dict(
            annotated="⟨As {S'|one} {V'|becomes} {C'|older and more experienced}⟩, {S|human knowledge} {V|is accumulated} and {S|beliefs} {V|are deepened}, ⟨while on the other hand {S'|the physical strength (to interact sincerely with the Other ⟨on an individual basis⟩)} {V'|decreases}⟩.",
            notes=["As＋比較級「〜するにつれて」。",
                   "【空所(b)】accumulated：is accumulated は受動態。and の後の are deepened と同じ形。",
                   "【空所(c)】decreases：while 節の S' は the physical strength（単数）なので3単現の s が付く。",
                   "while「一方で」は対比を表す。"],
            ja="人は年を取り経験を積むにつれて、知識は蓄積され、信念は深まる。その一方で、個人として誠実に他者と関わるための体力は衰えていく。"),
        dict(
            annotated="{強調|It is} {S|this gap between overconfidence and physical weakness} {強調|that} {V|allows} {O|myths} {C|to emerge}.",
            notes=["It is ～ that … の強調構文。強調部分は主語の this gap ～。元の文は This gap … allows myths to emerge.",
                   "【空所(d)】emerge：allow O to do の do なので原形。",
                   "this gap＝前文の「知識・信念の増大（→過信）」と「体力の衰え（→弱さ）」のずれ。"],
            ja="神話が生まれるのを許すのは、まさにこの過信と体力の衰えとのずれなのである。"),
        dict(
            annotated="{S|Myths} {V|are} not {C|necessary} ⟨to coexist with the Other⟩.",
            notes=["to coexist は「〜するために」という目的を表す不定詞（副詞的用法）。"],
            ja="他者と共存するのに、神話は必要ない。"),
        dict(
            annotated="{S|[What {V'|is needed}]} {V|is} {C|a little strength and wisdom}.",
            notes=["What is needed is ～「必要なのは〜だ」。What 節（名詞節）が S。"],
            ja="必要なのは、少しばかりの力と知恵である。"),
    ]),
]

# ---------------------------------------------------------------------------
# マークアップ → プレーン文 / 注釈付き HTML
# ---------------------------------------------------------------------------
BRACKETS = "()[]⟨⟩<>"


def plain(s):
    out = re.sub(r"⟪[^⟫]*⟫", "", s)
    out = re.sub(r"\{[^|{}]+\|", "", out)
    while re.search(r"\{[^|{}]+\|", out):
        out = re.sub(r"\{[^|{}]+\|", "", out)
    out = out.replace("}", "")
    for b in BRACKETS:
        out = out.replace(b, "")
    out = re.sub(r"\s+", " ", out)
    out = re.sub(r"\s+([,.?:;])", r"\1", out)
    return out.strip()


def annotate(s):
    res, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "{":
            j = s.index("|", i)
            label = s[i + 1:j]
            sub = label.endswith("'")
            kind = "sub" if sub else "main"
            if label == "強調":
                kind = "emph"
            res.append(f'<span class="{kind} l-{label.rstrip(chr(39))}">'
                       f'<span class="tag"><span>{html.escape(label)}</span></span>')
            i = j + 1
        elif c == "}":
            res.append("</span>")
            i += 1
        elif c in BRACKETS:
            res.append(f'<span class="br">{html.escape(c)}</span>')
            i += 1
        else:
            res.append(html.escape(c))
            i += 1
    return "".join(res)


def label_html(label):
    """Vt → V＋小さい t、仮S → 小さい仮＋S のように整形する。"""
    m = re.fullmatch(r"(仮|真)?([SVOCM])('*)(.*)", label)
    if not m:
        return html.escape(label)
    pre, core, primes, suf = m.groups()
    out = f"<small>{pre}</small>" if pre else ""
    out += core + primes
    if suf:
        out += f"<small>{html.escape(suf)}</small>"
    return out


def annotate_togi(s):
    """登木式：主節は丸囲みラベル＋黄/緑マーカー、従属節は ' 付きラベル、準動詞は ( ) ラベル。"""
    res, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "{":
            j = s.index("|", i)
            label = s[i + 1:j]
            if label.startswith("("):
                kind = "lv3"
            elif "'" in label:
                kind = "sub"
            elif label == "強調":
                kind = "emph"
            elif label.endswith("M"):
                kind = "main mm"
            else:
                kind = "main"
            res.append(f'<span class="{kind}"><span class="tag"><span>{label_html(label)}</span></span>')
            i = j + 1
        elif c == "}":
            res.append("</span>")
            i += 1
        elif c == "⟪":
            j = s.index("⟫", i)
            res.append(f'<span class="gap"><span class="tag"><span>{html.escape(s[i + 1:j])}</span></span>●</span>')
            i = j + 1
        elif c in BRACKETS:
            res.append(f'<span class="br">{html.escape(c)}</span>')
            i += 1
        else:
            res.append(html.escape(c))
            i += 1
    return "".join(res)


# ---------------------------------------------------------------------------
# 設問解説
# ---------------------------------------------------------------------------
ANSWERS = [
    ("(47)", "4", "Contact with that which is foreign prompts a quest for national identity.",
     "[A] 第1文「国家のアイデンティティの探求は、異質な存在との遭遇による既存の前提への挑戦への反応として現れる」の言い換え。"
     "1 は「記録がないから起源を創作せざるを得ない」と因果が違う（記録の乏しさは創作に“都合がよい”だけ）。2 の alien species（異星人）は alien existence の誤読。3 は本文にない。"),
    ("(48)", "3", "Theories on Japan's history are based on astrologers' horoscopes.（本文に“ない”もの）",
     "星座（constellations）は「断片を線でつないで形を作る」ことのたとえにすぎず、占星術の話ではない。"
     "1・2 は第3文（対外関係が変わるたびに説が変わった）、4 は第4文（論者の潜在意識の表現）に合う。"),
    ("(49)", "5", "b & d",
     "筆者が「疑っていない」のは事実として述べている内容。b は第1文「多くの人が起源についての考えに基づいて現代日本社会を論じている」と一致する。"
     "d は第3文「暗黙の前提がある」と一致する。a と c はその暗黙の前提そのもので、筆者は第2文の修辞疑問で疑っている。"),
    ("(50)", "1", "conditions",
     "the international ___ of the nineteenth century that allowed Japan to … の空所には「日本を〜させた19世紀の国際的な状況」が入る。international conditions が自然。"),
    ("(51)", "6", "rule",
     "a colonial ___ under which borders were drawn up：「その下で国境が引かれた植民地支配」。直後の a policy of rule through division とも対応する。"),
    ("(52)", "0", "boundaries",
     "borders were drawn up despite traditional ethnic ___：「伝統的な民族の境界を無視して国境が引かれた」。borders（国境）と boundaries（民族の境界線）を対比している。"),
    ("(53)", "2", "labour",
     "alien peoples … were introduced to provide ___：「労働力を供給するために異民族が連れてこられた」。プランテーションなどへの移民労働の話。toil も「労苦」の意味だが、provide labour が定型の言い方。"),
    ("(54)", "8", "ii → iv → iii → i",
     "ii（Furthermore で [E] の「日本が経験しなかったこと」に追加）→ iv（Nor で ii の否定を受けて「植民地支配も長くなかった」）"
     "→ iii（If … divided and ruled で [E] の分割統治の話を仮定法で展開）→ i（the two＝iii の南部と北部の人々。might have been も iii の仮定法を引き継ぐ）。"),
    ("(55)", "3", "entire（5番目）",
     "to (attempt to explain the entire world with a single) story。attempt to do「〜しようと試みる」、explain A with B「B で A を説明する」。"
     "並びは attempt(1) to(2) explain(3) the(4) entire(5) world(6) with(7) a(8) single(9)。"),
    ("(56)", "5", "single（9番目）", "上の並べ替えの9番目。a single story「たった一つの物語」。"),
    ("(57)", "3", "(a) criticising (b) accumulated (c) decreases (d) emerge",
     "(a) as in ～ing の前置詞 in の後ろなので動名詞。substituting と並列する。(b) is ___ and beliefs are deepened：受動態の過去分詞。"
     "(c) S' が the physical strength（単数）で現在形なので decreases。(d) allows myths to ___：to の後ろなので原形 emerge。"),
]

LOGIC = [
    ("A", "一般論の提示", "国家アイデンティティの探求は「異質な存在との遭遇」への反応として生まれる → そのとき歴史は行動指針の貯蔵庫として「創作」される → 起源は資料が乏しい先史時代に属するので、創作に特に都合がよい。",
     "本文全体の前提となる命題：「起源の歴史は、他者との遭遇をきっかけに“創られる”」。"),
    ("B", "日本への適用", "日本民族起源論に定説はない → 星座のように、資料の断片を各自が好きにつないで説を作る → 説は対外関係が変わるたびに変化した → 論者は潜在意識を語っているにすぎない。",
     "[A] の一般論を日本に当てはめた具体化。「起源論は事実ではなく、語る人の願望の反映」という批判的な視点が出てくる。"),
    ("C", "起源論が好まれる理由", "過去を自由に語ることほど魅力的なものはない → 例：単一民族・騎馬民族・聖書の民・南方の農耕民 → 起源論が人気なのは「夢を生きる」最良の方法だから。",
     "[B] を受けて「なぜそんな根拠の薄い議論がはやるのか」を説明する。起源論は事実ではなく「夢」だという評価。"),
    ("D", "問題提起（批判）", "今も起源論をもとに「日本人の性格」や現代社会を論じる人が多い → だが数千年前と現代に何の関係があるのか（修辞疑問） → 両者を結ぶのは「古代人もすでに日本人で、性格も不変」という暗黙の前提だけ。",
     "起源論から現代を語る議論の“隠れた前提”を暴く、本文の批判の中心。"),
    ("E", "反証（均質性の本当の理由）", "日本が比較的均質だとしても、理由は19世紀の国際条件にある（植民地化はされず、大帝国にもならなかった） → 民族の境界を無視した国境線や分割統治、労働移民の受け入れを経験しなかった。",
     "[D] の前提（太古から不変の日本人）への反論。均質性は「民族の本質」ではなく「近代の歴史・政治の結果」だと示す。"),
    ("F", "補強と仮定", "遠隔地に進出せず、植民地支配も短かった（→移民の流入なし） → もし分割統治されていたら、南と北の日本人は別民族に分類され、それを裏づける人類学理論さえあったかもしれない。",
     "仮定法で「民族の区分そのものが政治によって作られうる」ことを示し、[E] の主張を強める。"),
    ("G", "一般化（神話の背後）", "日本に限らず、ほぼすべての国民国家が起源神話を作ってきた → 神話は英雄的に見えるが、その背後にあるのは「現実からの逃避願望」。",
     "話題を日本から国民国家一般の「神話」へ広げ、その動機を示す転換の段落。"),
    ("H", "神話化の本質の分析", "過去の神話化の本質＝他者と向き合う恐怖からの逃避＋現在の分類を過去に投影すること → ステレオタイプはある程度必要（譲歩） → しかし他者を避け、単一の物語で世界を説明するのは他者の否定・抑圧である → これがあらゆる神話の起源。",
     "譲歩→逆接の型で、神話の本質を「他者の否定」と結論づける。本文の理論的な核心。"),
    ("I", "結論と提言", "ある神話を別の神話で置き換える（単一民族神話→混合民族神話）だけでは不十分 → すべての神話から自分を解放すべき → 年を取ると知識・信念は増えるが、他者と誠実に関わる体力は衰え、その“過信と体力の衰えのずれ”が神話を生む → 共存に神話は要らず、必要なのは少しの力と知恵。",
     "全体の結論。[H] の「神話＝他者からの逃避」を受けて、「他者と直接向き合う力と知恵をもて」と提言する。"),
]


def build():
    parts = []
    # --- 1. 完成本文 ---------------------------------------------------------
    body = []
    for label, sents in PARAS:
        txt = " ".join(plain(s["annotated"]) for s in sents)
        body.append(f'<div class="para"><span class="plabel">[{label}]</span><p>{html.escape(txt)}</p></div>')
    body.append('<p class="footnote">*homogeneous: Ethnically, culturally, linguistically and/or socially uniform/the same.</p>')

    ans_rows = "".join(
        f"<tr><td class='qn'>{q}</td><td class='an'>{a}</td><td>{html.escape(t)}</td></tr>"
        for q, a, t, _ in ANSWERS)
    ans_detail = "".join(
        f"<div class='qa'><div class='qh'><span class='qn'>{q}</span> 正解 <b>{a}</b>　<span class='qt'>{html.escape(t)}</span></div><p>{html.escape(e)}</p></div>"
        for q, a, t, e in ANSWERS)

    parts.append(f"""
<section class="sec">
  <h2><span class="num">1</span>設問の解答と完成本文</h2>
  <h3>解答一覧</h3>
  <table class="answers"><thead><tr><th>設問</th><th>正解</th><th>内容</th></tr></thead><tbody>{ans_rows}</tbody></table>
  <h3>設問解説</h3>
  {ans_detail}
</section>
<section class="sec page">
  <h3>完成本文（空所に正解を入れ、[F] は正しい順に並べた本文）</h3>
  <div class="fulltext">{''.join(body)}</div>
</section>""")

    # --- 2. 全和訳 -----------------------------------------------------------
    tr = "".join(
        f'<div class="para"><span class="plabel">[{label}]</span><p>{"".join(s["ja"] for s in sents)}</p></div>'
        for label, sents in PARAS)
    parts.append(f"""
<section class="sec page">
  <h2><span class="num">2</span>全和訳</h2>
  <div class="translation">{tr}</div>
</section>""")

    # --- 3. 文構造 -----------------------------------------------------------
    flat = [(label, s) for label, sents in PARAS for s in sents]
    assert len(flat) == len(TOGI)
    for (label, s), (tl, _, ann, _) in zip(flat, TOGI):
        assert label == tl and plain(ann) == plain(s["annotated"]), (plain(ann), plain(s["annotated"]))
    blocks = []
    prev = None
    for n, ((label, s), (_, pattern, ann, tnotes)) in enumerate(zip(flat, TOGI), 1):
        if label != prev:
            blocks.append(f'<h3 class="ph">段落 [{label}]</h3>')
            prev = label
        notes = "".join(f"<li>{html.escape(x)}</li>" for x in tnotes)
        blocks.append(f"""
<div class="sent">
  <div class="sn">{n}</div>
  <div class="pattern">{html.escape(pattern)}</div>
  <div class="en togi">{annotate_togi(ann)}</div>
  <ul class="notes">{notes}</ul>
  <div class="ja"><span class="jt">訳</span>{s['ja']}</div>
</div>""")
    demo = annotate_togi("{S|S} {Vt|V} {O|O} {M|M}")
    parts.append(f"""
<section class="sec page">
  <h2><span class="num">3</span>文構造（S・V・O・C 書き込み）</h2>
  <div class="legend togi">
    <div><b>記号の見方</b>（『英文読解戦略』プリントの表記に合わせています）</div>
    <div>{demo}　<b>主節（レベル①）</b>：黄色＝S・V・O・C（主役・中心・抽象）、緑色＝M（修飾語・具体・説明）。ラベルは丸囲み（tactics 001・037）</div>
    <div>V の右下：<b>i</b>＝自動詞（Vi）、<b>t</b>＝他動詞（Vt）、<b>受</b>＝受身（be＋p.p.）</div>
    <div><b>従属節（レベル②）</b>：S'・V'・O'・C'・M'（さらに内側は S''・V''…）。関係詞の内側で名詞が欠けている位置は <span class="gap">●</span>（S'欠・O'欠）</div>
    <div><b>準動詞（レベル③）</b>：ing・to do・p.p. の内側のミクロ文型は (V)(O)(M) で表す（tactics 034）</div>
    <div><span class="br">[ ]</span> 名詞のカタマリ　<span class="br">( )</span> 形容詞のカタマリ　<span class="br">&lt; &gt;</span> 副詞のカタマリ（tactics 037）</div>
    <div>仮S・真S：形式主語 It と真主語　強調：It is 〜 that … の強調構文</div>
  </div>
  {''.join(blocks)}
</section>""")

    # --- 4. 論理展開 ---------------------------------------------------------
    rows = "".join(f"""
<div class="lg">
  <div class="lg-h"><span class="plabel">[{l}]</span><span class="role">{r}</span></div>
  <div class="lg-b"><p class="flow">{html.escape(f)}</p><p class="func">▶ {html.escape(fn)}</p></div>
</div>""" for l, r, f, fn in LOGIC)

    parts.append(f"""
<section class="sec page">
  <h2><span class="num">4</span>論理展開</h2>
  <h3>段落ごとの論理展開</h3>
  {rows}
</section>
<section class="sec page">
  <h3>全体の論理展開</h3>
  <div class="overview">
    <div class="block"><div class="bh">序論 [A]〜[C]　起源論とは何か</div>
      <p>一般論：起源の歴史は、他者との遭遇をきっかけに「創作」される [A]<br>→ 日本の起源論も、対外関係とともに変わる論者の願望の表れ [B]<br>→ 起源論が人気なのは、それが「夢を生きる」手段だから [C]</p></div>
    <div class="arrow">▼</div>
    <div class="block"><div class="bh">本論① [D]〜[F]　起源論から現代日本を語ることへの批判</div>
      <p>「古代から日本人で性格も不変」という暗黙の前提への疑問 [D]<br>→ 反証：日本の均質性は19世紀の国際条件という近代の偶然の産物 [E]<br>→ 補強：分割統治されていれば南北で別民族とされた可能性（民族区分は政治的に作られる）[F]</p></div>
    <div class="arrow">▼</div>
    <div class="block"><div class="bh">本論② [G]〜[H]　神話一般の本質</div>
      <p>どの国家も起源神話をもつが、その背後にあるのは現実逃避の願望 [G]<br>→ 神話化の本質＝他者と向き合う恐怖からの逃避と、単一の物語による他者の否定・抑圧 [H]</p></div>
    <div class="arrow">▼</div>
    <div class="block conclusion"><div class="bh">結論 [I]　すべての神話からの解放</div>
      <p>神話を別の神話に置き換えるのではなく、あらゆる神話から自分を解放すべき。<br>他者と共存するのに必要なのは神話ではなく、少しの力と知恵である。</p></div>
  </div>
  <h3>要旨（150字程度）</h3>
  <p class="summary">国家の起源の歴史は、異質な他者との遭遇を機に創作されるものであり、日本民族起源論も論者の願望の表れにすぎない。日本の均質性も太古からの本質ではなく、19世紀の国際条件の産物である。起源神話の本質は他者と向き合う恐怖からの逃避と他者の抑圧にあり、私たちは神話を置き換えるのではなく、あらゆる神話から自らを解放し、少しの力と知恵で他者と共存すべきである。</p>
  <h3>読解のポイント</h3>
  <ul class="points">
    <li><b>キーワード「the Other（他者）」</b>：[A] の an alien existence、[B] の the outside world が、[H]・[I] で the Other としてまとめられる。「他者からの逃避が神話を生む」が一貫した主張。</li>
    <li><b>「神話（myth）」の意味の広がり</b>：前半は「日本民族の起源論」、[G] 以降は「国民国家の起源神話」から「単一の物語で世界を説明すること」全般へ広がる。</li>
    <li><b>具体→抽象の構成</b>：一般論 [A] → 日本の具体例 [B]〜[F] → 再び一般化 [G]〜[H] → 結論 [I] というサンドイッチ型。</li>
    <li><b>対比</b>：単一民族神話と混合民族神話（どちらも神話）／知識・信念の増大と体力の衰え（過信と弱さのずれ）。</li>
  </ul>
</section>""")

    css = (HERE / "style.css").read_text(encoding="utf-8")
    doc = f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><title>英語長文 V 解答・解説</title>
<style>{css}</style></head>
<body>
<header class="cover">
  <div class="kicker">英語長文 V</div>
  <h1>国家の起源と「神話」<br><small>解答・全訳・文構造・論理展開</small></h1>
  <ol class="toc">
    <li>設問の解答と完成本文</li><li>全和訳</li><li>文構造（S・V・O・C 書き込み）</li><li>論理展開（段落ごと・全体）</li>
  </ol>
</header>
{''.join(parts)}
</body></html>"""
    OUT.write_text(doc, encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    build()
