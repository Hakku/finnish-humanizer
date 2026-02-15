# Finnish Humanizer

Tunnistaa ja poistaa AI-generoidun suomenkielisen tekstin tunnusmerkit. Tekee tekstistä luonnollisempaa ja ihmisen kirjoittaman kuuloista.

## Kenelle

Kaikille jotka tuottavat suomenkielistä tekstiä AI:n avulla ja haluavat lopputuloksen kuulostavan ihmiseltä: markkinointi, journalismi, dokumentaatio, viestintä.

## Mitä skill tunnistaa

26 AI-patternia jaettuna kahteen ryhmään:

**Suomenkieliset (1–12):** Passiivin ylikäyttö, nominaalirakenteet, pronominien ylikäyttö, puuttuvat partikkelit, käännösrakenteet, genetiiviketjut, adjektiivikasaumat, ylipitkät virkkeet, joka/jotka-kasautuminen, virkakielisyys, astevaihtelun välttely, liiallinen kohteliaisuus.

**Universaalit suomeksi (13–26):** Merkittävyyden liioittelu, mainosmainen kieli, mielistelevä sävy, liiallinen varautuminen, täytesanat, geneerinen lopetus, epämääräiset viittaukset, "haasteista huolimatta" -kaava, kolmen sääntö ja synonyymikierto, partisiippirakenteet, kopulan välttely, negatiivinen rinnastus, keinotekoiset skaalaviittaukset, tietokatkos-vastuuvapauslausekkeet.

**4 tyylimerkintää:** Lihavoinnin ylikäyttö, emojit, "Otsikko:" -listaus, kaarevat lainausmerkit.

Täysi patternilista esimerkkeineen: [`finnish-humanizer/references/patterns.md`](finnish-humanizer/references/patterns.md)

## Asennus

### Claude.ai (ZIP-upload)

1. [Lataa `finnish-humanizer.zip`](https://github.com/Hakku/finnish-humanizer/releases/latest/download/finnish-humanizer.zip)
2. Avaa [claude.ai](https://claude.ai)
3. Luo uusi projekti (tai avaa olemassa oleva)
4. Lisää ZIP projektin **Project knowledge** -osioon

### Claude.ai (manuaalinen)

1. Luo projekti [claude.ai](https://claude.ai):ssä
2. Mene projektin asetuksiin → **Custom instructions**
3. Kopioi `finnish-humanizer/SKILL.md`:n sisältö instructions-kenttään
4. Lisää `finnish-humanizer/references/patterns.md` projektin tiedostoihin (**Project knowledge**)

### Claude Code (`~/.claude/skills/`)

1. Kopioi `finnish-humanizer/`-kansio (sisältää `SKILL.md` + `references/`) polkuun `~/.claude/skills/finnish-humanizer/`
2. Käynnistä Claude Code uudelleen (skill-lista ladataan session alussa)
3. Kutsu: `/finnish-humanizer [tiedostopolku tai teksti]`

**CC-lisäasetukset:** Lisää frontmatteriin `argument-hint: "[tiedostopolku tai teksti]"` saadaksesi käyttövinkin slash-komennon yhteyteen.

### API (`container.skills`)

Lisää SKILL.md:n sisältö system-promptiin ja patterns.md kontekstina. Tarkemmat ohjeet riippuvat käyttämästäsi API-clientistä.

## Käyttö

Liitä suomenkielinen teksti keskusteluun ja pyydä luonnollistamaan:

```
Luonnollista tämä teksti:

[tekstisi tähän]
```

Muita toimivia komentoja:

- "Poista AI-tuntu tästä tekstistä"
- "Tee tästä ihmismäisempää"
- "Humanisoi tämä"

### Lyhyt vs. pitkä teksti

- **Alle 500 sanaa:** Skill käsittelee suoraan ja palauttaa luonnollistetun version + muutosyhteenvedon.
- **Yli 500 sanaa:** Skill analysoi ensin, esittää löydetyt patternit ja kysyy epäselvistä ennen toteutusta.

### Muutosyhteenveto

Oletuksena skill palauttaa tekstin lisäksi lyhyen listan tehdyistä muutoksista. Jos haluat pelkän tekstin:

```
Luonnollista tämä teksti. Älä selitä muutoksia.
```

## Rajoitukset

- Toimii vain suomenkieliselle tekstille
- Ei muuta asiasisältöä — vain esitystapaa
- Ei yksinkertaista — virallinen teksti pysyy virallisena
- Ei korvaa ihmisen editointia — poistaa AI-tunnusmerkkejä, ei tee tekstistä "hyvää"

## Lisenssi

MIT — katso [LICENSE](LICENSE)
