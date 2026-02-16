# Finnish Humanizer — GPT Builder Configuration

## Name

Finnish Humanizer — Luonnollista suomea

## Description (short, for GPT Store listing)

Tunnistaa ja poistaa AI-generoidun suomenkielisen tekstin tunnusmerkit. 26 patternia + 4 tyylimerkintää. Liimaa teksti, saat luonnollisen version takaisin.

## Instructions

Kopioi `instructions.md` sisältö GPT Builder → Instructions -kenttään.

**Merkkimäärä:** ~6 500 merkkiä (raja 8 000)

## Knowledge Files

Lataa seuraava tiedosto GPT Builder → Knowledge -osioon:

| Tiedosto | Kuvaus |
|----------|--------|
| `patterns.md` | Täysi 26 patternin lista esimerkkeineen + 4 tyylimerkintää + täysimittainen ennen/jälkeen -esimerkki |

## Conversation Starters

1. **Liimaa teksti tähän, niin luonnollistan sen**
2. **Analysoi ensin — mitä AI-patterneita tämä teksti sisältää?**
3. **Luonnollista tämä blogipostaus säilyttäen virallinen sävy**
4. **Onko tämä teksti luonnollista vai AI-generoitua?**

## Capabilities

| Capability | Enabled | Miksi |
|------------|---------|-------|
| Web Search | Ei | Ei tarvetta — toimii offline-tekstinkäsittelynä |
| Canvas | Kyllä | Pitkien tekstien muokkaus canvas-tilassa on luontevaa |
| Image Generation | Ei | Tekstinkäsittelytyökalu, ei tarvitse kuvia |
| Code Interpreter | Ei | Ei tarvetta |

## Publishing Settings

| Asetus | Arvo |
|--------|------|
| Visibility | Everyone (Public) |
| Category | Writing |
| Builder profile | Hakku |

## Avatar

Minimalistinen ikoni: suomen lipun värit (sininen/valkoinen) + kynä tai tekstisymboli. Tai yksinkertainen "FI" tekstisymboli puhtaalla taustalla.

**Vaihtoehto:** Generoi GPT Builder → Create -välilehdellä automaattisesti.

## Testing Checklist (2.2)

Testaa ennen julkaisua 10 tekstillä:

- [x] Blogipostaus (epämuodollinen)
- [x] Markkinointiteksti (mainosmainen)
- [x] Some-julkaisu (lyhyt)
- [x] Tekninen dokumentaatio
- [x] Virallinen raportti
- [x] Sähköpostiviesti
- [x] Jo luonnollinen teksti (ei muutoksia tarvita) — korjattu: kriittiset säännöt kohta 1
- [x] Sekateksti (fi/en)
- [x] Koodidokumentaatio (koodiesimerkit säilyvät)
- [x] Pitkä teksti (>500 sanaa) — korjattu: käyttäjän triggeröimä "analysoi"-tila




## Julkaisun jälkeen

1. Kopioi GPT:n linkki
2. Lisää linkki finnish-humanizer -repon README:hen
3. Jaa linkki suomenkielisille sisällöntuottajaryhmille
