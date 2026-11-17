#!/usr/bin/env python3
"""英語長文 III（Huntington, Who Are We?）の解答・解説 HTML を生成する。

表記・レイアウトは長文 V（build.py）と共通。PDF化は render.js で行う:
  python3 build/build_iii.py && node build/render.js passage_iii.html english_passage_III_solution.pdf
"""
import html
import pathlib

from build import annotate_togi, plain

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "passage_iii.html"

# 本文中の ( ) [ ] はカタマリ記号として消えるので、文字どおりの括弧はこの代替文字で書く
LITERAL = {"⦅": "(", "⦆": ")", "⁅": "[", "⁆": "]"}


def lit(s):
    for k, v in LITERAL.items():
        s = s.replace(k, v)
    return s


# ---------------------------------------------------------------------------
# 本文データ  (段落, 空所番号 or None, 文型, 注釈付き英文, 構文メモ, 和訳)
#   注釈の記法は syntax.py の冒頭を参照（登木式）
# ---------------------------------------------------------------------------
S = [
    # ---- 第1段落 ----
    ("1", None, "SVC（第2文型）",
     "{M|<For almost three centuries>} {S|religion} {V|was} {C|a declining factor (in human affairs)}.",
     ["be 動詞が V なので SVC（tactics 011）。S＝C：宗教＝衰えつつある要因（tactics 019）。",
      "declining は現在分詞の前置修飾「衰えつつある」。"],
     "ほぼ3世紀にわたって、宗教は人間の営みにおいて衰えつつある要因であった。"),
    ("1", None, "SVO（第3文型）",
     "{M|<In the seventeenth century>}, {M|<after more than a hundred years of bloody religious war>}, {S|the leaders (of Europe)} {M|<in the Treaty of Westphalia>} {Vt|attempted to reduce and contain} {O|the influence (of religion) (in politics)}.",
     ["文頭の M が2つ続く → S を探す（tactics 027）。",
      "attempt to do はまとめて V（tactics 017）。reduce と contain が and で並び、O を共有している（tactics 029）。"],
     "17世紀、100年以上にわたる血なまぐさい宗教戦争の後、ヨーロッパの指導者たちはウェストファリア条約において、政治における宗教の影響力を弱め、封じ込めようとした。"),
    ("1", "25", "SVO（第3文型）",
     "{M|<In the following century>}, {S|Enlightenment thinkers} {Vt|exalted} {O|reason} {M|<over faith>} {M|<as a source of human understanding>}.",
     ["【25】b。In the following century＝前文の17世紀の「次の世紀」＝18世紀。後ろの文が19世紀なので時系列がつながる。",
      "exalt A over B「B よりも A を高く評価する」。as 〜 は「〜として」の M。"],
     "次の世紀には、啓蒙思想家たちが、人間の理解の源として、信仰よりも理性を高く評価した。"),
    ("1", None, "SVO（第3文型）＋同格",
     "{S|The nineteenth century} {Vt|saw} {O|increasing confidence} {M|[that {S'|science} {V't|would dethrone} {O'|religion}]}.",
     ["無生物主語＋see「S（時代）には〜が見られた」。",
      "confidence の後ろの that 節は同格（名詞のシゴト⑦：tactics 003）。従接の that なので内側は完全文（tactics 033②）。",
      "dethrone「王座から引きずり下ろす」。"],
     "19世紀には、科学が宗教をその座から引きずり下ろすだろうという確信が強まった。"),
    ("1", None, "SV（第1文型）",
     "{S|Mankind}, {M|<it was widely believed>}, {Vi|was moving} {M|<into a new phase (of rationalism, pragmatism, and secularism)>}.",
     ["it was widely believed は挿入。元は It was widely believed that mankind was moving 〜。",
      "move は「S 自身が空間移動する」系の完全自動詞（tactics 008）。into 〜 は M。"],
     "人類は合理主義、実用主義、世俗主義という新しい段階へと進みつつあると、広く信じられていた。"),
    ("1", None, "SVC（第2文型）",
     "{S|Religious beliefs}, {M|<Sigmund Freud argued in The Future of an Illusion>}, {V|were} {C|“insusceptible to proof”} and {C|“incompatible with everything ({S'|we} {V't|have discovered} ⟪O'欠⟫ {M'|<about the reality of the world>})”}.",
     ["Sigmund Freud argued 〜 は挿入（「〜とフロイトは論じた」）。",
      "C が2つ（insusceptible／incompatible）で、and でつながる（tactics 029）。",
      "everything の後ろは目的格の関係代名詞 that が省略された形容詞のカタマリ。内側は discovered の O' が欠けている（tactics 031）。"],
     "宗教的信念は「証明できず」、「我々が世界の実相について発見してきたあらゆることと相いれない」と、ジークムント・フロイトは『ある幻想の未来』で論じた。"),
    ("1", None, "SVC（第2文型）",
     "{S|They} {V|were}, {M|<in short>}, {C|“delusions.”}",
     ["They＝Religious beliefs。in short「要するに」は挿入の M。"],
     "要するに、宗教的信念は「妄想」だというのである。"),
    # ---- 第2段落 ----
    ("2", "26", "SVO（第3文型）",
     "{S|Modernization and modernity} {Vt|appeared to be undermining} {O|religion}, {M|(which ⟪S'欠⟫ {V'受|was held to be} {C'|a dark holdover (from the past)})}.",
     ["【26】d。第1段落の「科学・合理主義が宗教を退ける」流れを受け、後ろの「西洋で宗教が周辺化した」具体例につなぐ。",
      "appear to do「〜するように見える」はまとめて V（tactics 017）。",
      "コンマ＋which は非制限用法。先行詞は religion。hold O to be C「O を C とみなす」の受身なので、C' が残る（tactics 018）。"],
     "近代化と近代性は宗教を衰えさせつつあるように見え、宗教は過去からの暗い遺物とみなされていた。"),
    ("2", None, "SVO, SVC, and SVO（等位接続）",
     "{M|<Outside the United States>} {S|fewer people (in the Western world)} {Vt|practiced} {O|religion}, {S|churches} {V|were} {M|increasingly} {C|empty}, and {S|religious beliefs and religious institutions} {Vt|came to play} {O|a minor and peripheral role} {M|<in most Western societies>}.",
     ["A, B, and C の形で3つの文が並ぶ。V は practiced・were・came to play の3個（V の数の法則：tactics 010）。",
      "come to do「〜するようになる」はまとめて V（tactics 017）。",
      "fewer people practiced 〜「〜する人が減った」。"],
     "アメリカ以外の西洋世界では、宗教を実践する人が減り、教会はますます空になり、宗教的信念や宗教制度は、ほとんどの西洋社会でささいで周辺的な役割しか果たさなくなった。"),
    ("2", None, "SV（第1文型）",
     "{M|<In the public arena>}, {S|religion} {Vi|gave way} {M|<to ideology>}.",
     ["give way to 〜「〜に取って代わられる・道を譲る」。to 〜 は M。"],
     "公的な領域では、宗教はイデオロギーに取って代わられた。"),
    ("2", None, "SV（受身：SVO → SV）",
     "{S|People, governments, social movements} {V受|were defined} {M|<by their identification with one (of the major secular ideologies)>}: {M|liberalism, socialism, communism, fascism, authoritarianism, corporatism, democracy}.",
     ["define の受身なので O が1つ減って SV（tactics 018）。",
      "their identification with 〜「自分を〜と同一視すること」。",
      "コロン以下は the major secular ideologies の具体的な中身（同格：tactics 003）。"],
     "人々も、政府も、社会運動も、主要な世俗的イデオロギー――自由主義、社会主義、共産主義、ファシズム、権威主義、コーポラティズム、民主主義――のどれかと自らを同一視することによって規定された。"),
    ("2", None, "SVO＋VO＋VO（等位接続）",
     "{S|These ideologies} {Vt|dominated} {O|political debate}, {Vt|shaped} {O|domestic and international alignments and conflicts}, and {Vt|provided} {O|models (for [how {S'|countries} {V't|could organize} {O'|their politics and economies}])}.",
     ["V が3個（dominated・shaped・provided）で、S は共通（tactics 010・029）。",
      "how 節は前置詞 for の後ろの名詞のカタマリ（tactics 028）。how の内側は完全文。"],
     "これらのイデオロギーが政治論争を支配し、国内外の連携や対立を形づくり、国家が政治や経済をどう組織すればよいかのモデルを提供した。"),
    # ---- 第3段落 ----
    ("3", None, "SV（受身：SVO → SV）",
     "{M|<In the last quarter (of the twentieth century)>}, however, {S|the march (toward secularism)} {V受|was reversed}.",
     ["however が転換の合図。ここから「世俗化」→「宗教の復興」へ流れが逆転する。",
      "reverse の受身なので SV（tactics 018）。"],
     "しかし20世紀の最後の四半世紀に、世俗主義へ向かう歩みは逆転した。"),
    ("3", "27", "SV（第1文型）＋分詞構文",
     "{S|An almost global resurgence (of religion)} {Vi|got under way}, {M|<manifest in almost every part of the world — except in Western Europe>}.",
     ["【27】a。前文の「世俗化の逆転」を具体化し、except in Western Europe が次の文の Elsewhere「（西欧以外の）よその地域では」と対応する。",
      "get under way「始まる」はまとめて V（自動詞）。",
      "manifest は形容詞「明らかな」。being が省略された分詞構文と考える（＝and it was manifest in 〜）。"],
     "ほぼ世界規模の宗教の復興が始まり、それは世界のほとんどあらゆる地域で――西ヨーロッパを除いて――はっきりと見られた。"),
    ("3", None, "SVO（第3文型）",
     "{M|<Elsewhere in countries all over the world>}, {S|religious political movements} {Vt|gained} {O|supporters}.",
     ["Elsewhere＝「西ヨーロッパ以外の場所では」。前文の except in Western Europe を受ける。"],
     "西欧以外の世界中の国々では、宗教的な政治運動が支持者を獲得した。"),
    ("3", None, "SVC（第2文型）＋not A but B",
     "And {M|<in these countries>}, {S|the most religious people} {V|have not been} {C|elderly, but young} and {C|not poor peasants but upwardly mobile, well-educated white-collar workers and professional people (epitomized {(M)|<by the female medical school students in Turkey (who ⟪S'欠⟫ {V't|defied} {O'|their secular government} {M'|<by wearing Islamic headdress to class>})>})}.",
     ["not A but B「A ではなく B」が2回：not elderly but young／not poor peasants but 〜 people。どちらも C（tactics 029）。",
      "epitomized by 〜 は過去分詞の後置修飾で、〜 people にかかる M。「〜に代表される」。",
      "who の内側は S' が欠けた文（tactics 031）。by wearing 〜「〜を着用することで」。"],
     "そしてこれらの国々で最も信心深い人々は、高齢者ではなく若者であり、貧しい農民ではなく、社会的に上昇しつつある高学歴のホワイトカラー労働者や専門職の人々であった。その典型が、イスラムのスカーフを着けて授業に出ることで世俗的な政府に逆らったトルコの女子医学生たちである。"),
    ("3", None, "SV and VO（等位接続）",
     "{S|The two great missionary religions}, {M|Islam and Christianity}, {Vi|are competing} {M|worldwide} {M|<for converts>} and {Vt|gaining} {O|them}, {M|<most notably in Muslim fundamentalist movements and evangelical Protestantism, (which ⟪S'欠⟫ {V't|has had} {O'|a tremendous impact} {M'|<in Latin America>} and {V't|is now influencing} {O'|Africa, Asia, and the former Soviet world})>}.",
     ["Islam and Christianity は S の同格（tactics 003）。",
      "are competing と (are) gaining が and で並ぶ（tactics 029）。them＝converts（改宗者）。",
      "コンマ＋which の先行詞は evangelical Protestantism（has が単数なので）。内側は V' が2つ（has had／is now influencing）。"],
     "二大布教宗教であるイスラム教とキリスト教は、世界中で改宗者を奪い合い、実際に獲得している。とりわけ顕著なのはイスラム原理主義運動と福音派プロテスタントであり、後者はラテンアメリカに多大な影響を与え、今やアフリカ、アジア、旧ソ連圏にも影響を及ぼしつつある。"),
    ("3", None, "SVO（コロン以下が O の内容）",
     "{S|An exhaustive quantitative report (on global religion) (during the late twentieth century)} {Vt|concluded} {M|bluntly}: {O|“{S'|the majority (of countries) (in the ⁅developing⁆ world)}, {M'|<with a majority of the global population>}, {V'i|are} {M'|<in the midst of a religious resurgence>}.}",
     ["conclude の中身がコロン以下の引用。引用の中は S'V'i（be＝「存在する」）。",
      "with a majority of the global population は挿入の M'（「世界人口の過半数を抱えて」）。",
      "be in the midst of 〜「〜のただ中にある」。[developing] は引用者（筆者）が補った語。"],
     "20世紀後半の世界の宗教に関する網羅的な定量的報告書は、率直にこう結論づけた。「（発展途上）世界の国々の大多数は、世界人口の過半数を抱えながら、宗教復興のただ中にある。"),
    ("3", None, "SVO（第3文型）",
     "{S|The resurgence} {Vt|is most strongly affecting} {O|former Communist countries (of Eastern Europe, Central Asia, and the Caucasus), as well as Latin America, the Middle East, Africa, China, and South East Asia}.”",
     ["A as well as B「B だけでなく A も」。A＝former Communist countries 〜（most strongly の対象）、B＝Latin America 以下。",
      "引用はこの文で終わる。"],
     "その復興は、東欧・中央アジア・コーカサスの旧共産主義諸国に最も強く影響を及ぼしており、さらにラテンアメリカ、中東、アフリカ、中国、東南アジアにも及んでいる」。"),
    ("3", "28", "SVC（第2文型）＋付帯状況",
     "{M|<Within the developed world>}, {M|<in contrast>}, {S|religion} {V|seems to be} {C|on the decline} {M|<in most countries>}, {M|<with the most notable exception being the United States>}.",
     ["【28】h。直前の報告書の引用は「発展途上（developing）世界」の話。h の Within the developed world, in contrast が「先進世界では対照的に」と対比になる。",
      "seem to be C はまとめて V と見て SVC（tactics 017・019）。on the decline「衰退して」。",
      "with O 〜ing は付帯状況。O＝the most notable exception、being the United States＝「最も顕著な例外はアメリカである」。"],
     "それとは対照的に、先進世界ではほとんどの国で宗教は衰退しているように見える。最も顕著な例外はアメリカである。"),
    ("3", None, "SV（受身）",
     "{S|The resurgence} {V受|has been duly noted} {M|<by scholars, (who ⟪S'欠⟫ {V't|published} {O'|books (titled {(C)|The Revenge of God, Questioning the Secular State, and Secularism in Retreat})})>}.",
     ["The resurgence は第3段落の主題「宗教の復興」を受け直している。h（先進国の話）を挟んでも、話題は復興に戻る。",
      "who の内側は S' が欠けた文。titled は過去分詞で books にかかる。title O C「O に C という題をつける」の受身なので、後ろに C が残る。"],
     "この復興は学者たちにもしかるべく注目され、彼らは『神の復讐』『世俗国家を問う』『後退する世俗主義』といった題の本を出版した。"),
    # ---- 第4段落 ----
    ("4", "29", "SV（第1文型）",
     "{S|The twenty-first century} {Vi|is beginning} {M|<as an age of religion>}.",
     ["【29】g。段落の主題文（トピック・センテンス）。直後の「西洋型の世俗国家モデルが挑戦を受けている」と、各国の具体例（イラン・ロシア・トルコ・インド…）の総論になる。",
      "begin はここでは自動詞「始まる」（tactics 008：S 自身が出現する系）。as 〜 は「〜として」の M。"],
     "21世紀は宗教の時代として幕を開けつつある。"),
    ("4", None, "SV（受身：進行形）",
     "{S|Western secular models (of the state)} {V受|are being challenged and replaced}.",
     ["be being p.p. は進行形の受身「〜されつつある」。challenged と replaced が and で並ぶ。"],
     "西洋的な世俗国家のモデルは、挑戦を受け、取って代わられつつある。"),
    ("4", None, "SVC（第2文型）",
     "{M|<In Iran>}, {S|the Pahlavi shah's effort (to create a modernizing, secular, Western state)} {V|fell} {C|victim} {M|<to the Islamic Revolution>}.",
     ["fall victim to 〜「〜の犠牲になる」。fall は「〜の状態になる」で SVC（S＝C：努力＝犠牲）。",
      "to create は effort にかかる形容詞のカタマリ（M）。"],
     "イランでは、近代化を進める世俗的な西洋型国家を築こうとしたパフラヴィー朝の国王の試みが、イスラム革命の犠牲となった。"),
    ("4", None, "SV（第1文型）",
     "{M|<In Russia>}, {S|Lenin's secular and anti-religious Soviet state} {Vi|has given way} {M|<to a Russian state (that ⟪S'欠⟫ {V't|terms} {O'|the Orthodox Church} {C'|central to “the establishment and development of Russia's spirituality and culture.”})>}",
     ["give way to 〜「〜に取って代わられる」（第2段落の religion gave way to ideology と同じ表現。今度は逆に世俗国家が宗教寄りの国家に道を譲る）。",
      "that の内側は S' が欠けた文。term O C「O を C と呼ぶ・位置づける」の SVOC。"],
     "ロシアでは、レーニンの世俗的で反宗教的なソビエト国家が、ロシア正教会を「ロシアの精神性と文化の確立と発展」の中心に据えるロシア国家に取って代わられた。"),
    ("4", None, "SVC, and SVO and VO",
     "{M|<In Turkey>}, {S|Mustafa Kemal Atatürk's vision (of a Westernized, secular nation state)} {V|has been} {C|under challenge} {M|<from an increasingly powerful Islamist political movement>}, and {S|a religiously defined political party} {Vt|won} {O|an election} and {Vt|formed} {O|a government} {M|<in 2002>}.",
     ["前半：be under challenge「挑戦を受けている」（前置詞句が C）。",
      "後半：S は共通で V が2つ（won／formed）。and が2個 → 文と文、V と V の2段階の等位接続（tactics 010・029）。"],
     "トルコでは、西洋化された世俗的な国民国家というムスタファ・ケマル・アタテュルクの構想が、ますます力を増すイスラム主義の政治運動から挑戦を受けており、2002年には宗教色の強い政党が選挙に勝って政権を樹立した。"),
    ("4", None, "SV and SVO and VO",
     "{S|Nehru's concept (of India) (as a secular, socialist, parliamentary democracy)} {Vi|came} {M|<under attack>} {M|<by several political and religious movements>} and {S|their affiliate}, {M|the BJP ⦅Indian People's Party⦆}, {Vt|scored} {O|an electoral victory} and {Vt|took} {O|control (of the government)}.",
     ["come under attack「攻撃を受ける」。",
      "and の後ろに新しい S（their affiliate）があり、V が scored／took の2つ。the BJP は their affiliate の同格（tactics 003）。",
      "their＝several political and religious movements。affiliate「関連組織・提携団体」。"],
     "インドを世俗的・社会主義的な議会制民主主義国家とするネルーの構想は、いくつもの政治的・宗教的運動から攻撃を受け、それらと連携する政党 BJP（インド人民党）が選挙で勝利して政権を握った。"),
    ("4", "30", "SV（受身：SVO → SV）",
     "{S|The primary national founder Ben-Gurion's image (of Israel) (as a secular Jewish social democracy)} {V受|has been repudiated} {M|<by Orthodox Jewish groups>}.",
     ["【30】e。イラン→ロシア→トルコ→インドと「建国者・指導者の世俗国家構想が宗教勢力に否定された」例が並ぶ。イスラエル（ベン＝グリオン）も同じ型の例で、次のアラブ世界の例の前に入る。",
      "image of A as B「A を B とみなす像」。repudiate「否定する・拒絶する」の受身で SV（tactics 018）。"],
     "建国の父ベン＝グリオンが描いた、世俗的なユダヤ人の社会民主主義国家としてのイスラエル像は、正統派ユダヤ教徒の集団によって否定されている。"),
    ("4", None, "SVO（第3文型）",
     "{M|<In the Arab world>}, {S|a scholar (of comparative politics)} {Vt|has shown} {O|[that {S'|a “new nationalism”} {V'i|is emerging}, {M'|<{(V)|fusing} {(O)|the formerly antagonistic old nationalism (of the Nasser era) and the now increasingly powerful currents (of political Islam)}>}]}.",
     ["that 節は名詞のカタマリで O（tactics 028）。内側は完全文。",
      "fusing 〜 は分詞構文。ing にもミクロ文型があり (V)(O) と読める（tactics 034）。fuse A and B「A と B を融合する」。",
      "formerly antagonistic「かつては敵対していた」⇔ now increasingly powerful「今やますます強力な」の対比。"],
     "アラブ世界では、ある比較政治学者が、かつては敵対していたナセル時代の古いナショナリズムと、今やますます力を増している政治的イスラムの潮流とを融合した「新しいナショナリズム」が生まれつつあることを明らかにした。"),
    ("4", None, "SVO（第3文型）",
     "{M|<Where {S'|elections} {V'受|have been held} {M'|<in the Arab world>}>}, {S|Islamist political parties} {M|almost consistently} {Vt|increased} {O|their strength} {M|<around the start of the new century>}.",
     ["Where は「〜するところでは」という副詞節（M）を作る。"],
     "アラブ世界で選挙が行われたところでは、新世紀の初めごろ、イスラム主義政党がほぼ一貫して勢力を伸ばした。"),
    ("4", "31", "SV（第1文型）",
     "{M|<Throughout the world>}, {S|these political leaders}, {M|<as {S'|one sociologist} {V't|put} {O'|it}>}, {Vi|have been “striving} {M|<for new forms (of national order) (based on religious values)>}.”",
     ["【31】f。段落のまとめ。these political leaders は、直前まで挙げた各国の宗教的な政治運動・政党（イスラム革命、BJP、イスラム主義政党など）を指す。Throughout the world も「イラン・ロシア・トルコ・インド・イスラエル・アラブ」の例をまとめる言い方。",
      "as one sociologist put it「ある社会学者の言葉を借りれば」は挿入。",
      "strive for 〜「〜を求めて努力する」。based on 〜 は過去分詞で forms にかかる M。"],
     "世界中で、こうした政治指導者たちは、ある社会学者の言葉を借りれば、「宗教的価値観に基づく新しい形の国家秩序を目指して奮闘」してきたのである。"),
]

# ---------------------------------------------------------------------------
# 設問
# ---------------------------------------------------------------------------
OPTIONS = [
    ("a", "An almost global resurgence of religion got under way, manifest in almost every part of the world — except in Western Europe.",
     "ほぼ世界規模の宗教の復興が始まり、世界のほとんどあらゆる地域で――西ヨーロッパを除いて――はっきりと見られた。"),
    ("b", "In the following century, Enlightenment thinkers exalted reason over faith as a source of human understanding.",
     "次の世紀には、啓蒙思想家たちが、人間の理解の源として信仰よりも理性を高く評価した。"),
    ("c", "Islamic militants, both religious and secular, do see America, its people, its religion, and its civilization as Islam's enemy.",
     "宗教的であれ世俗的であれ、イスラムの過激派は、アメリカとその国民・宗教・文明をイスラムの敵とみなしている。"),
    ("d", "Modernization and modernity appeared to be undermining religion, which was held to be a dark holdover from the past.",
     "近代化と近代性は宗教を衰えさせつつあるように見え、宗教は過去からの暗い遺物とみなされていた。"),
    ("e", "The primary national founder Ben-Gurion's image of Israel as a secular Jewish social democracy has been repudiated by Orthodox Jewish groups.",
     "建国の父ベン＝グリオンの「世俗的なユダヤ人の社会民主主義国家」というイスラエル像は、正統派ユダヤ教徒の集団に否定されている。"),
    ("f", "Throughout the world, these political leaders, as one sociologist put it, have been “striving for new forms of national order based on religious values.”",
     "世界中で、こうした政治指導者たちは、ある社会学者の言葉を借りれば「宗教的価値観に基づく新しい形の国家秩序を目指して奮闘」してきた。"),
    ("g", "The twenty-first century is beginning as an age of religion.",
     "21世紀は宗教の時代として幕を開けつつある。"),
    ("h", "Within the developed world, in contrast, religion seems to be on the decline in most countries, with the most notable exception being the United States.",
     "対照的に先進世界では、ほとんどの国で宗教は衰退しているように見える。最も顕著な例外はアメリカである。"),
]

ANSWERS = [
    ("(25)", "b",
     "前文は17世紀（ウェストファリア条約）、直後は The nineteenth century（19世紀）。b の In the following century「その次の世紀」＝18世紀の啓蒙思想が入ると、17→18→19世紀の時系列がつながる。"
     "内容も「理性＞信仰」で、段落の主題「宗教の衰退」に合う。a は20世紀末の宗教復興の話なので、ここに入れると段落の流れと矛盾する。"),
    ("(26)", "d",
     "第1段落末の「宗教は妄想（フロイト）」を受け、第2段落の冒頭で「近代化が宗教を掘り崩し、宗教は過去の遺物とみなされた」とまとめる。"
     "直後の「西洋で宗教を実践する人が減り、教会が空になった」はその具体的な現れ。"),
    ("(27)", "a",
     "直前の文は「20世紀最後の四半世紀に世俗化の歩みが逆転した」。a の「ほぼ世界規模の宗教の復興が始まった」がその具体化。"
     "a の except in Western Europe と、直後の Elsewhere「（西欧以外の）よその地域では」がぴったり対応する。"),
    ("(28)", "h",
     "直前の報告書の引用は「発展途上（developing）世界の大多数の国で宗教が復興している」。h の Within the developed world, in contrast「対照的に先進世界では」が developing ⇔ developed の対比になる。"
     "28 に g を入れたくなるが、in contrast を含む h はここ以外に入る場所がない。"),
    ("(29)", "g",
     "第4段落の主題文。「21世紀は宗教の時代として始まりつつある」→「西洋型の世俗国家モデルが挑戦を受け、取って代わられつつある」→ イラン・ロシア・トルコ・インド…の具体例、という「抽象→具体」の流れ。"),
    ("(30)", "e",
     "イラン（パフラヴィー国王）→ロシア（レーニン）→トルコ（アタテュルク）→インド（ネルー）と、「建国者・指導者の世俗国家構想が宗教勢力に否定された」例が国ごとに並ぶ。"
     "e のイスラエル（ベン＝グリオン）はまさに同じ型で、アラブ世界の例の前に入る。"),
    ("(31)", "f",
     "最後に各国の例をまとめる文。these political leaders が、直前まで挙げた宗教的な政治運動・政党（イスラム革命、BJP、イスラム主義政党など）を指す。"
     "Throughout the world も、各国の例を「世界中で」と総括する表現。"),
]
UNUSED = ("c", "イスラム過激派が「アメリカを敵視している」という内容。本文は世界的な宗教の復興と世俗国家モデルの後退を論じていて、アメリカと対立する話はどこにも出てこないので、入る空所がない。")

LOGIC = [
    ("第1段落", "世俗化の歴史（17〜19世紀）",
     "約3世紀にわたり宗教は衰退 → 17世紀：宗教戦争の後、ウェストファリア条約で政治から宗教を切り離す → 18世紀：啓蒙思想が理性を信仰より上位に置く【25 b】 → 19世紀：科学が宗教を退けるという確信 → フロイト「宗教は妄想」。",
     "時代順に「宗教が衰えていく流れ」を示し、後の「逆転」の前提をつくる段落。"),
    ("第2段落", "20世紀：宗教の周辺化",
     "近代化が宗教を掘り崩し、宗教は過去の遺物とされた【26 d】 → 西洋（米国以外）では信仰の実践が減り、宗教は周辺的な役割に → 公の場ではイデオロギーが宗教に取って代わる → 自由主義・社会主義などの世俗的イデオロギーが政治を支配。",
     "世俗化が完成した状態の描写。「宗教→イデオロギー」への交代。"),
    ("第3段落", "転換：世界的な宗教の復興",
     "however：20世紀最後の四半世紀に世俗化が逆転 → 西欧を除く世界規模の宗教復興【27 a】 → 担い手は若く高学歴の人々（例：トルコの女子医学生） → イスラム教・キリスト教（福音派）が信者を拡大 → 報告書：途上国の大多数で宗教復興 → 対照的に先進国では宗教は衰退（例外は米国）【28 h】 → 学者もこの復興に注目。",
     "本文の核心となる転換点。「誰が」「どこで」「どう」復興しているかを具体的に示し、先進国との対比も加える。"),
    ("第4段落", "政治への影響：世俗国家モデルの後退",
     "21世紀は宗教の時代【29 g】 → 西洋型の世俗国家モデルが挑戦を受けている → イラン・ロシア・トルコ・インド・イスラエル【30 e】・アラブ世界の具体例 → 世界中で指導者が宗教的価値観に基づく国家秩序を目指している【31 f】。",
     "「主題文 → 具体例の列挙 → まとめ」の典型的な段落構成。宗教の復興が国家・政治のあり方まで変えていることを示す。"),
]


# ---------------------------------------------------------------------------
def build():
    parts = []
    paras = []
    for p, blank, _, ann, _, ja in S:
        if not paras or paras[-1][0] != p:
            paras.append((p, []))
        paras[-1][1].append((blank, ann, ja))

    # --- 1. 解答・完成本文 ---------------------------------------------------
    ans_rows = "".join(
        f"<tr><td class='qn'>{q}</td><td class='an'>{a}</td><td>{html.escape(dict((k, t) for k, t, _ in OPTIONS)[a])}</td></tr>"
        for q, a, _ in ANSWERS)
    ans_rows += f"<tr><td class='qn'>不要</td><td class='an'>{UNUSED[0]}</td><td>{html.escape(OPTIONS[2][1])}</td></tr>"
    ans_detail = "".join(
        f"<div class='qa'><div class='qh'><span class='qn'>{q}</span> 正解 <b>{a}</b></div><p>{html.escape(e)}</p></div>"
        for q, a, e in ANSWERS)
    ans_detail += f"<div class='qa'><div class='qh'>使わない選択肢 <b>{UNUSED[0]}</b></div><p>{html.escape(UNUSED[1])}</p></div>"
    opt_rows = "".join(
        f"<tr><td class='qn'>{k}</td><td>{html.escape(en)}<div class='opt-ja'>{html.escape(ja)}</div></td></tr>"
        for k, en, ja in OPTIONS)

    body = []
    for p, sents in paras:
        txt = []
        for blank, ann, _ in sents:
            t = html.escape(lit(plain(ann)))
            if blank:
                t = f'<span class="fill"><span class="bn">{blank}</span>{t}</span>'
            txt.append(t)
        body.append(f'<div class="para"><span class="plabel">{p}</span><p>{" ".join(txt)}</p></div>')

    parts.append(f"""
<section class="sec">
  <h2><span class="num">1</span>設問の解答と完成本文</h2>
  <h3>解答一覧</h3>
  <table class="answers"><thead><tr><th>設問</th><th>正解</th><th>入る文</th></tr></thead><tbody>{ans_rows}</tbody></table>
  <h3>設問解説</h3>
  {ans_detail}
</section>
<section class="sec page">
  <h3>選択肢と和訳</h3>
  <table class="answers options"><tbody>{opt_rows}</tbody></table>
  <h3>完成本文（空所に正解を入れた本文。網かけが空所）</h3>
  <div class="fulltext">{''.join(body)}</div>
  <p class="footnote">Adapted from Samuel P. Huntington, <i>Who Are We?: The Challenges to America's National Identity</i></p>
</section>""")

    # --- 2. 全和訳 -----------------------------------------------------------
    tr = "".join(
        f'<div class="para"><span class="plabel">{p}</span><p>{"".join(ja for _, _, ja in sents)}</p></div>'
        for p, sents in paras)
    parts.append(f"""
<section class="sec page">
  <h2><span class="num">2</span>全和訳</h2>
  <div class="translation">{tr}</div>
</section>""")

    # --- 3. 文構造 -----------------------------------------------------------
    blocks, prev = [], None
    for n, (p, blank, pattern, ann, notes, ja) in enumerate(S, 1):
        if p != prev:
            blocks.append(f'<h3 class="ph">第{p}段落</h3>')
            prev = p
        li = "".join(f"<li>{html.escape(x)}</li>" for x in notes)
        mark = f'<span class="pattern blank">空所 {blank}</span> ' if blank else ""
        blocks.append(f"""
<div class="sent">
  <div class="sn">{n}</div>
  {mark}<div class="pattern">{html.escape(pattern)}</div>
  <div class="en togi">{lit(annotate_togi(ann))}</div>
  <ul class="notes">{li}</ul>
  <div class="ja"><span class="jt">訳</span>{ja}</div>
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
  </div>
  {''.join(blocks)}
</section>""")

    # --- 4. 論理展開 ---------------------------------------------------------
    rows = "".join(f"""
<div class="lg">
  <div class="lg-h"><span class="plabel">{l}</span><span class="role">{r}</span></div>
  <div class="lg-b"><p class="flow">{html.escape(f)}</p><p class="func">▶ {html.escape(fn)}</p></div>
</div>""" for l, r, f, fn in LOGIC)
    parts.append(f"""
<section class="sec page">
  <h2><span class="num">4</span>論理展開</h2>
  <h3>段落ごとの論理展開</h3>
  {rows}
  <h3>全体の論理展開</h3>
  <div class="overview">
    <div class="block"><div class="bh">第1〜2段落　世俗化の時代（17世紀〜20世紀半ば）</div>
      <p>宗教戦争の後、政治から宗教を切り離す → 啓蒙思想・科学が宗教を退ける<br>→ 近代化で宗教は過去の遺物に。公の場では世俗的イデオロギーが宗教に取って代わる</p></div>
    <div class="arrow">▼ however（逆転）</div>
    <div class="block"><div class="bh">第3段落　世界的な宗教の復興（20世紀末〜）</div>
      <p>西欧を除く世界中で宗教が復興。担い手は若く高学歴の人々<br>→ 途上国の大多数で復興 ⇔ 先進国では衰退（例外はアメリカ）</p></div>
    <div class="arrow">▼</div>
    <div class="block conclusion"><div class="bh">第4段落　21世紀＝宗教の時代</div>
      <p>西洋型の世俗国家モデルが各国で挑戦を受け、取って代わられつつある<br>（イラン・ロシア・トルコ・インド・イスラエル・アラブ世界）<br>→ 世界中で、宗教的価値観に基づく国家秩序が目指されている</p></div>
  </div>
  <h3>要旨（150字程度）</h3>
  <p class="summary">17世紀以降、宗教は政治から切り離され、啓蒙思想や科学、近代化によって衰退し、20世紀には世俗的イデオロギーがその役割を担った。しかし20世紀末に流れは逆転し、西欧を除く世界中で、とりわけ若く高学歴の人々を担い手として宗教が復興した。21世紀は宗教の時代として始まり、各国で西洋型の世俗国家モデルが宗教的価値観に基づく国家秩序に取って代わられつつある。</p>
  <h3>読解・解答のポイント</h3>
  <ul class="points">
    <li><b>時を表す語で並べる</b>：In the seventeenth century → In the following century【25 b】 → The nineteenth century → In the last quarter of the twentieth century → The twenty-first century【29 g】。時系列の語は文補充の最大の手がかり。</li>
    <li><b>対比の語を探す</b>：except in Western Europe【27 a】⇔ Elsewhere／developing world ⇔ Within the developed world, in contrast【28 h】。in contrast を含む文は、何と対比しているかを本文中で必ず確認する。</li>
    <li><b>指示語の指す先</b>：these political leaders【31 f】は前に具体例が並んだ後でないと使えない → 段落の最後に入る。</li>
    <li><b>具体例の型をそろえる</b>：「建国者・指導者の世俗国家構想 → 宗教勢力による挑戦・否定」の型で国ごとの例が並ぶので、同じ型の e（ベン＝グリオン）が【30】に入る。</li>
    <li><b>主題文は段落の頭</b>：g は抽象的な総論なので、具体例が続く第4段落の冒頭【29】に置く。</li>
    <li><b>キーワード「give way to」</b>：第2段落では宗教がイデオロギーに道を譲り、第4段落ではソビエトの世俗国家が宗教寄りのロシア国家に道を譲る。同じ表現で「立場の逆転」を示している。</li>
  </ul>
</section>""")

    css = (HERE / "style.css").read_text(encoding="utf-8")
    doc = f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><title>英語長文 III 解答・解説</title>
<style>{css}</style></head>
<body>
<header class="cover">
  <div class="kicker">英語長文 III</div>
  <h1>宗教の復興と世俗国家の後退<br><small>解答・全訳・文構造・論理展開</small></h1>
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
