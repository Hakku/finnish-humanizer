# Finnish Humanizer: Jakelustrategia

## Tilanne

Multi-platform expansion (v1.1.0) on valmis. Repo tukee 15 alustaa ja build.py generoi dist-tiedostot automaattisesti. Seuraava vaihe: sisällön viimeistely ja jakelu.

## Ongelma

Kukaan ei löydä repoa. 15 alustatukea on hyödytön ilman jakelua. GitHub-haku ei tuo suomenkielistä niche-työkalua esiin orgaanisesti.

## Tutkimustulokset (helmikuu 2026)

### Jakelukanavat

| Kanava | Tähdet/koko | Tyyppi |
|--------|-------------|--------|
| awesome-cursorrules | 37.7K | Cursor-säännöt, PR-pohjainen |
| awesome-claude-code | 21.6K | Claude Code skills/hooks/CLAUDE.md |
| awesome-copilot | 21.4K | Virallinen GitHub-repo, instructions/agents |
| cursor.directory | 800+ templatea | Web-hakemisto, ei GitHub-tähtiä |
| awesome-clinerules | pieni | Cline-säännöt |

### Kohderyhmät

| Kohderyhmä | Koko | Kanava | Motivaatio |
|-----------|------|--------|------------|
| Suomalaiset kehittäjät | ~100K | Cursor, Copilot, Claude Code | Docs, README:t, koodikommentit suomeksi |
| Suomalaiset sisältötuottajat | ~500K+ | ChatGPT, Gemini | Blogit, markkinointitekstit, raportit |
| Kansainväliset kehittäjät | miljoonia | Awesome-listat, GitHub-haku | Kiinnostus kielityökaluihin, inspiraatio omille |

### Kilpailija-analyysi: blader/humanizer

[blader/humanizer](https://github.com/blader/humanizer) — 4 885 tähteä (1 kk:ssa), 382 forkkia. Englanninkielinen, vain Claude Code, 24 patternia Wikipedia-pohjalta.

**Päällekkäisyys:** ~15 universaalia patternia yhteistä (merkittävyyden liioittelu, mainosmainen kieli, mielistelevä sävy jne.)

**Finnish-humanizerin uniikki arvo:** 12 suomenkielistä patternia (passiivin ylikäyttö, puuttuvat partikkelit, käännösrakenteet, genetiiviketjut jne.) + 15 alustan multi-platform-tuki + build-automaatio.

**blader/humanizerin vahvuus:** PERSONALITY AND SOUL -osio on laajempi ja konkreettisempi kuin `<finnish_voice>`. Wikipedia-lähde on auktoritatiivinen.

### Päätökset

1. **Ei englanninkielistä versiota.** Kilpailisi suoraan 4.9K-tähden vakiintunutta repoa vastaan ilman ainutlaatuista arvoa. FI-spesifisyys on kilpailuetu.
2. **README pidetään lyhyenä.** Pitkät perustelut ja taustat erillisiin docs-sivuihin tarvittaessa.
3. **`<finnish_voice>` -osio parannetaan ennen launchia.** Inspiraatio blader:in PERSONALITY AND SOUL -osiosta. Ks. Vaihe 0.
4. **Some-julkaisut valmistellaan.** LinkedIn (Tekoälyt testissä ym. yhteisöt), X (suomeksi ja englanniksi), Facebook.
5. **HN/Reddit odotetaan awesome-list PR:ien mergeä.**
6. **Arvioidaan EN-versio uudelleen** jos blader/humanizer ei laajene multi-platform-tueksi 3kk:n sisällä.

### Oletukset

1. Awesome-list PR:t hyväksytään jos ne ovat laadukkaita ja relevantteja
2. Suomenkielinen niche-työkalu on uniikki lisäarvo näihin listoihin (ei kilpailijoita)
3. Englanninkielinen README-osio parantaa GitHub-haun löydettävyyttä merkittävästi
4. cursor.directory hyväksyy ulkoisia kontribuutioita
5. Repo on GitHubissa (Hakku/finnish-humanizer), julkinen

## Suunnitelma

### Vaihe 0: `<finnish_voice>` -osion parannus

**Miksi:** Skillin ydinlaatu ennen jakelua. blader/humanizer osoittaa, että "soul"-ohjaus on kriittinen — pelkkä patternien poisto ei riitä.

**Status:** VALMIS (2026-02-17). Tutkimus + sparraus (6 kierrosta) + toteutus.

#### 0.1 Tutkimustulokset (synteesi)

Kolme rinnakkaista tutkimusagenttia suoritettiin: (a) suomalainen kirjoitusääni, (b) blader/humanizer-analyysi, (c) AI-tekstin tunnistaminen suomeksi. Yhteensä 16+ verkkohakua, 20+ lähdettä.

**Suomalaisen kirjoitusäänen ydinpiirteet (tutkimustulokset):**

| Piirre | Lähde | Relevanssi skilliin |
|--------|-------|---------------------|
| **Klapi-proosa** — lakoninen minimalismi, tiukkuus, ulkoapäin kuvaava | Britannica, Words Without Borders (Meri, Hyry, Vartio) | Vahvistaa "lyhyys" ja "suoruus" -periaatteita |
| **Substantiivitauti** — "toteuttaa tekemisen" kun voisi "tehdä" | Kotus, Politiikasta | Jo patterneissa (#2), mutta puuttuu voice-osiosta |
| **Liitepartikkelit** (-hAn, -pA, -kin, -kAAn) kantavat pragmaattista/interpersoonaalista merkitystä | UGA, De Gruyter | Vahvistaa "partikkelit"-periaatetta — ne eivät ole "sävy" vaan merkitys |
| **Ellipsi (sananheitto)** — jo mainittu jätetään pois | Tieteen termipankki, Wikipedia FI | PUUTTUU voice-osiosta kokonaan. Kriittinen lisäys. |
| **Sanajärjestyksen vapaus** — teema-reema, painotus loppuun | Helsingin yliopisto, Kielitoimisto | PUUTTUU voice-osiosta. AI tuottaa jäykkää SVO:ta. |
| **Kuiva huumori** — understatement, deadpan | RatherBeInFinland, Suomainen.com | Osittain "innostus epäilyttää" -kohdassa, mutta ei eksplisiittinen |
| **Rekisterien sekoittaminen** — puhe/kirjakieli luontevasti | TalkPal, Kielitoimisto | PUUTTUU. AI kirjoittaa joko liian virallista tai kömpelyä puhekieltä. |
| **"Omaaaninen kirjoittaminen"** (OPH) — oma ääni vs. geneerinen | OPH, Plotti | Vahvistaa "persoonallisuuden lisääminen" -konseptia |

**blader/humanizer PERSONALITY AND SOUL (~38 riviä):**

| Konsepti | Suomalainen vastine | Toimenpide |
|----------|---------------------|------------|
| "Signs of soulless writing" (6 kohtaa) | Universaali — toimii suoraan suomeksi | Lisätään "Sieluttoman tekstin tunnusmerkit" -lista |
| "Have opinions" | "Ota kantaa" — ei vain raportoi, reagoi | Lisätään persoonallisuus-osioon |
| "Vary your rhythm" | Jo "Rytmin vaihtelu" -kohdassa | Säilytetään, vahvistetaan |
| "Acknowledge complexity" | Jo "Monimutkaisuuden tunnustaminen" | Säilytetään |
| "Use I when it fits" | Suomessa verbikonjugaatio korvaa pronominin — periaate pätee mutta mekanismi eri | Ei lisätä sellaisenaan |
| "Let some mess in" | Jo "Harkittu epätäydellisyys" | Säilytetään |
| "Be specific about feelings" | "Ole spesifinen" — universaali | Yhdistetään "Spesifisyys"-kohtaan |

**AI-teksti suomeksi (ongelmat):**
- Ei suomenkielisiä AI-detektoreita (kaikki kv:t, koulutettu EN-datalla)
- "Sutu" = suomalainen termi AI-slopille
- Humanizer.fi dokumentoinut: yliformaalisuus, kontekstiin sopimattomat sanavalinnat, jäykkä virkerakenne, monotoninen rytmi, ylitoisto, "liian täydellinen ja persoonaton"
- Juurisyy: mallit "ajattelevat" englanniksi ja kääntävät suomeksi

#### 0.2 Konkreettinen `<finnish_voice>` -muutosehdotus

**Muutosstrategia:** Laajenna 32 → ~41 riviä (+9). Kompensoidaan leikkaamalla `<examples>`-osiosta 1 kanoninen esimerkki (säästö ~6 riviä). Tavoite: SKILL.md ≤ 160 riviä.

**Muutokset yksityiskohtaisesti:**

| # | Muutos | Peruste |
|---|--------|---------|
| 1 | Periaatteet säilytetään ja tiivistetään hieman (6 → 7 kpl) | Tutkimus vahvisti kaikki nykyiset periaatteet |
| 2 | "Hiljaisuus on tyylikeino" → **"Ellipsi on luonnollista"** | Tutkimus: sananheitto on oma kielen ilmiö, vahvempi kuin yleinen "hiljaisuus" |
| 3 | **UUSI: "Sanajärjestys on työkalu"** | Tutkimus: teema-reema puuttuu kokonaan, AI:n jäykkä SVO on yksi selvimmistä tunnusmerkeistä |
| 4 | Partikkelit-kohtaa vahvistetaan: "turhia" → "kantavat merkitystä" | Tutkimus: pragmaattinen/interpersoonaalinen funktio, ei vain "elävöittäminen" |
| 5 | **UUSI osio: "Sieluttoman tekstin tunnusmerkit"** (4 kohdan lista) | blader/humanizer-inspiraatio, suomalaistettu |
| 6 | Sieluton vs. elävä -esimerkki laajennetaan (lisää tekniikoita näkyviin) | Nykyinen "elävä" liian suppea, ei demonstroi voice-tekniikoita |
| 7 | "Persoonallisuuden lisääminen" → **"Miten persoonallisuutta lisätään"** | Uudelleennimetään, lisätään "Ota kantaa", vahvistetaan "Spesifisyys" |
| 8 | `<examples>`-osiosta poistetaan #6 Genetiiviketjut | Vapauttaa ~5 riviä. Esimerkki löytyy references/patterns.md:stä. |

**Luonnos — uusi `<finnish_voice>` (rivit ~23–63, 41 riviä):**

```markdown
<finnish_voice>
Ennen kuin korjaat yhtään patternia, sisäistä miten suomalainen kirjoittaja ajattelee.

**Suoruus.** Suomalainen sanoo asian ja siirtyy eteenpäin. Ei johdattelua, ei pehmentämistä. "Tämä ei toimi" on täysi lause.

**Lyhyys on voimaa.** Lyhyt virke ei ole laiska — se on täsmällinen. Pitkä virke on perusteltava.

**Toisto on sallittu.** Saman sanan käyttö kahdesti on normaalia. Synonyymikierto kuulostaa suomessa teennäiseltä.

**Innostus epäilyttää.** Kuiva toteamus on vahvempi kuin huutomerkki. "Ihan hyvä" on kehu.

**Ellipsi on luonnollista.** Jo mainittu jätetään pois — tämä on suomen kielen perusrakenne, ei laiskuutta. AI toistaa kaiken eksplisiittisesti. Luota lukijan muistiin.

**Partikkelit kantavat merkitystä.** -han/-hän, -pa/-pä, kyllä, vaan. Ne eivät ole turhia — ne ilmaisevat asennetta ja suhdetta lukijaan. AI jättää ne pois.

**Sanajärjestys on työkalu.** Virkkeen alku on tuttua tietoa, loppu uutta ja tärkeää. AI tuottaa jäykkää SVO:ta eikä hyödynnä sanajärjestyksen vapautta painottamiseen.

### Sieluttoman tekstin tunnusmerkit

Kieliopillisesti virheetön teksti voi olla kuollutta:
- Jokainen virke samanpituinen ja -rakenteinen
- Ei mielipiteitä, ei epävarmuutta — vain neutraalia raportointia
- Ei persoonaa: kuka tahansa olisi voinut kirjoittaa tämän
- Lukee kuin lehdistötiedote tai Wikipedia-artikkeli

**Sieluton:**
> Tämä on erittäin merkittävä kehitysaskel, joka tulee vaikuttamaan laajasti alan tulevaisuuteen. On syytä huomata, että kyseinen innovaatio tarjoaa lukuisia mahdollisuuksia eri sidosryhmille. Haasteista huolimatta tulevaisuus näyttää valoisalta.

**Elävä:**
> Iso juttu alalle. En ole varma mihin tämä lopulta johtaa, mutta hyötyjiä on — varsinkin ne jotka ovat odottaneet tällaista jo vuosia.

### Miten persoonallisuutta lisätään

Patternien poistaminen ei yksin riitä. Elävä teksti tarvitsee:
- **Rytmin vaihtelu.** Lyhyt virke. Sitten pidempi joka ottaa aikansa. Monotoninen rakenne paljastaa AI:n.
- **Ota kantaa.** Älä vain raportoi — reagoi. "En tiedä mitä tästä ajatella" on inhimillisempää kuin neutraali lista.
- **Tunnusta monimutkaisuus.** Asiat voivat olla ristiriitaisia tai keskeneräisiä. AI ratkaisee kaiken siististi.
- **Spesifisyys.** "Monet yritykset" → "Kolme suurinta kilpailijaa". Konkreettisuus on uskottavuutta.
- **Harkittu epätäydellisyys.** Sivujuonteet, itsekorjaus, ajatuksen kehittyminen kesken tekstin.
</finnish_voice>
```

**Rivibudjetti:**
- Nykyinen `<finnish_voice>`: 32 riviä → Uusi: ~41 riviä (+9)
- Nykyinen `<examples>`: 50 riviä → Uusi: ~44 riviä (-6, poistetaan #6 Genetiiviketjut)
- Netto: +3 riviä → SKILL.md ~154 riviä (alle 160 rajan)

#### 0.3 Avoimet kysymykset

1. **Poistetaanko #6 Genetiiviketjut vai jokin muu kanoninen esimerkki?** Genetiiviketjut on suomelle ominainen pattern mutta löytyy references/patterns.md:stä. Vaihtoehtoja: #13 Merkittävyyden liioittelu (universaali, vähemmän uniikki).
2. **Onko 160 rivin raja kova vai joustava?** Jos joustava, voitaisiin pitää kaikki 7 kanonista esimerkkiä ja mennä ~160 riviin.
3. **Tarvitseeko "elävä" -esimerkki olla pidempi?** Nykyinen luonnos on 1 virke pidempi kuin alkuperäinen. Riittääkö?

#### 0.4 Toteutusvaiheet

1. Editoi `<finnish_voice>` -osio SKILL.md:ssä yllä olevan luonnoksen mukaisesti
2. Poista tai vaihda 1 kanoninen esimerkki `<examples>`-osiosta (rivibudjetti)
3. Aja `py build.py` → dist päivittyy
4. Tarkista: ovatko dist-tiedostot valideja kaikille 15 alustalle

### Vaihe 1: Repon valmistelu jakeluun

**Miksi:** Awesome-list PR:t ohjaavat liikennettä repoon. Repon pitää olla valmis vastaanottamaan kävijöitä — myös englanninkielisiä.

**Mitä:**

1.1. **Englanninkielinen README-intro** (README.md alkuun)
- Lyhyt (5-10 riviä): "What is this?", "Quick start", linkki suomenkieliseen osioon
- Mahdollistaa GitHub-haun löydettävyyden (hakusanat: "AI text humanizer", "Finnish", "remove AI patterns")

1.2. **GitHub-repon metadata**
- Description (englanniksi): "Detects and removes AI-generated patterns from Finnish text. Custom instructions for 15+ AI platforms."
- Topics: `ai`, `finnish`, `humanizer`, `cursor-rules`, `copilot-instructions`, `claude-code`, `chatgpt`, `ai-writing`, `prompt-engineering`
- Nämä vaikuttavat suoraan GitHub-haun näkyvyyteen

1.3. **Commitoi multi-platform expansion** (v1.1.0)
- Kaikki muutokset yhdessä commitissa/PR:ssä
- Pitää olla mergettynä ennen awesome-list PR:iä

### Vaihe 2: Awesome-list PR:t (top 3)

**Miksi:** 80K+ tähden yhteisyleisö. Finnish Humanizer on ainoana suomenkielisenä työkaluna uniikki jokaisessa listassa.

**Mitä:**

2.1. **PR → awesome-cursorrules** (37.7K tähteä)
- Tutki repon kontribuutio-ohjeet ja PR-formaatti
- Lisää finnish-humanizer omaan kategoriaan (Language-specific / Localization)
- Linkki: `dist/cursor/finnish-humanizer.mdc`
- PR-viesti englanniksi, lyhyt kuvaus mitä skill tekee

2.2. **PR → awesome-claude-code** (21.6K tähteä)
- Tutki repon rakenne (skills-osio?)
- Lisää finnish-humanizer skills-listaan
- Linkki: `finnish-humanizer/SKILL.md` (CC:n natiivi formaatti)

2.3. **PR → awesome-copilot** (21.4K tähteä)
- Virallinen GitHub-repo, todennäköisesti tiukemmat kriteerit
- Linkki: `dist/copilot/finnish-humanizer.instructions.md`
- Korostus: kielikohtainen työkalu, täydentää englanninkielisiä ohjeita

**Status:** Muutama PR jo tehty. Tarkistetaan tilanne ja arvioidaan seuraavat.

### Vaihe 3: Some-julkaisut ja sekundääriset kanavat

**Miksi:** Awesome-listat ovat pitkän aikavälin orgaaninen liikenne. Some on nopea piikki joka tukee alkuvaiheen näkyvyyttä.

**Mitä:**

3.1. **Some-julkaisut** (odotetaan awesome-list PR:ien mergeä)
- **LinkedIn:** Tekoälyt testissä ja vastaavat yhteisöt. Suomeksi, ammattillinen sävy.
- **X:** Oma tili, sekä suomeksi että englanniksi. Lyhyt demo (ennen/jälkeen).
- **Facebook:** Oma tili, suomeksi.

3.2. **cursor.directory -hakemisto**
- Selvitä kontribuutiomalli (PR vai lomake?)

3.3. **awesome-clinerules**
- PR jos repo on aktiivinen

3.4. **Hacker News / Reddit**
- Ajoitetaan awesome-list mergejen jälkeen
- HN: "Show HN: Finnish Humanizer — remove AI patterns from Finnish text (26 patterns, 15 platforms)"
- Reddit: r/Suomi, r/ChatGPT, r/cursor

### Vaihe 4: Ylläpito ja seuranta

**Miksi:** Jakelukanavan avaaminen ei riitä — pitää seurata tuloksia ja reagoida.

**Mitä:**

4.1. **GitHub traffic -seuranta** (Settings → Traffic)
- Baselinea ennen PR:iä, mittaa vaikutus

4.2. **Star-count seuranta**
- Jos awesome-list PR tuo merkittävästi tähtiä, se validoi strategian

4.3. **Issue/PR -seuranta repossa**
- Kontribuutiot = signaalimerkki siitä, että työkalu on löydetty

4.4. **EN-version uudelleenarviointi** (3 kk:n jälkeen)
- Jos blader/humanizer ei laajene multi-platform-tueksi
- Tai jos kysyntää ilmenee (issues, some-viestit)

## Prioriteetti ja järjestys

```
Vaihe 0 (sisältölaatu)   ← ENSIN, skillin ydinlaatu
  0.1-0.2 <finnish_voice> parannus
  0.3-0.4 Rajoitustarkistus + rebuild
Vaihe 1 (valmistelu)     ← Repon julkaisukunto
  1.3 Commitoi v1.1.0
  1.1 Englanninkielinen README-intro
  1.2 GitHub-repon metadata
Vaihe 2 (top 3 kanavat)  ← SUURIN VAIKUTUS
  2.1 awesome-cursorrules PR
  2.2 awesome-claude-code PR
  2.3 awesome-copilot PR
Vaihe 3 (some + muut)    ← Odotetaan Vaihe 2 mergeä
  3.1 Some-julkaisut (LinkedIn, X, Facebook)
  3.2-3.4 cursor.directory, clinerules, HN/Reddit
Vaihe 4 (seuranta)       ← JATKUVA
```

## Avoimet kysymykset

1. ~~Repon nimi GitHubissa~~ → Julkinen, Hakku/finnish-humanizer
2. ~~`<finnish_voice>` laajuus~~ → Tutkimus tehty, luonnos valmis. Mahtuu ~154 riviin kun 1 kanoninen esimerkki poistetaan.
3. ~~HN/Reddit-ajoitus~~ → Odotetaan awesome-list mergeä
4. ~~README-intron laajuus~~ → Lyhyt (5-10 riviä)
5. ~~Englanninkielinen versio~~ → Ei nyt. Arvioidaan 3 kk:n päästä.
6. **Mikä kanoninen esimerkki poistetaan?** #6 Genetiiviketjut (suomi-spesifinen) vai #13 Merkittävyyden liioittelu (universaali)?
7. **Onko 160 rivin raja kova?** Jos ei, voidaan pitää kaikki 7 esimerkkiä.
