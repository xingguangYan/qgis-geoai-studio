# Journal Requirements & Paper Submission Reference

## Journal Classification & Tiers

### SCI/SSCI Journal Tiers
| Tier | IF Range | Examples |
|------|----------|----------|
| Q1 | > 5.0 | RSE (13.5), ISPRS JPRS (12.7), Nature (64.8), Science (56.9) |
| Q2 | 3.0-5.0 | Ecological Indicators (6.9), JAG (4.2), STOTEN (10.8) |
| Q3 | 1.5-3.0 | Remote Sensing (5.0), IEEE JSTARS (4.2), GIScience (3.0) |
| Q4 | < 1.5 | Various lower-tier journals |

### Key Remote Sensing & GIS Journals

| Journal | ISSN | IF 2024 | Type | Days to First Decision | Acceptance Rate |
|---------|------|---------|------|----------------------|-----------------|
| Remote Sensing of Environment (RSE) | 0034-4257 | 13.5 | SCI Q1 | 60-90 | ~20% |
| ISPRS JPRS | 0924-2716 | 12.7 | SCI Q1 | 45-75 | ~22% |
| IJAEOG | 1569-8432 | 7.5 | SCI Q1 | 60-90 | ~25% |
| JAG | 1569-8432 | 7.5 | SCI Q1 | 60-90 | ~25% |
| Ecological Indicators | 1470-160X | 6.9 | SCI Q1 | 90-120 | ~25% |
| STOTEN | 0048-9697 | 10.8 | SCI Q1 | 60-90 | ~30% |
| Remote Sensing (MDPI) | 2072-4292 | 5.0 | SCI Q2 | 30-60 | ~40% |
| Atmosphere (MDPI) | 2073-4433 | 3.1 | SCI Q3 | 30-60 | ~50% |
| Land (MDPI) | 2073-445X | 3.9 | SCI Q2 | 30-45 | ~45% |
| GIScience & Remote Sensing | 1548-1603 | 6.7 | SCI Q1 | 60-90 | ~25% |
| IEEE TGRS | 0196-2892 | 8.2 | SCI Q1 | 90-150 | ~25% |
| IEEE GRSL | 1545-598X | 4.0 | SCI Q2 | 60-90 | ~35% |
| JSTARS | 2151-1535 | 4.2 | SCI Q2 | 45-75 | ~35% |
| Sci. Total Environ. | 0048-9697 | 10.8 | SCI Q1 | 60-90 | ~30% |
| J. Cleaner Prod. | 0959-6526 | 11.1 | SCI Q1 | 90-120 | ~25% |
| Catena | 0341-8162 | 6.2 | SCI Q1 | 90-120 | ~25% |
| Geoderma | 0016-7061 | 6.1 | SCI Q1 | 90-150 | ~20% |
| Forest Ecology & Mgmt | 0378-1127 | 4.0 | SCI Q2 | 90-120 | ~25% |

### Chinese Core Journals (遥感/GIS相关)
| Journal | Type | Rank |
|---------|------|------|
| 遥感学报 | CSCD/Core | 中文核心 |
| 国土资源遥感 | CSCD | 中文核心 |
| 遥感技术与应用 | CSCD | 中文核心 |
| 地理学报 | CSCD | 卓越期刊 |
| 地理研究 | CSCD | 中文核心 |
| 地理科学 | CSCD | 中文核心 |
| 地理科学进展 | CSCD | 中文核心 |
| 地球信息科学学报 | CSCD | 中文核心 |
| 生态学报 | CSCD | 中文核心 |
| 环境科学 | CSCD/EI | 中文核心 |
| 农业工程学报 | EI | 中文核心 |
| 林业科学 | CSCD | 中文核心 |
| 应用生态学报 | CSCD | 中文核心 |
| 中国环境科学 | EI | 中文核心 |
| Science China Earth Sci. | SCI Q1 | 卓越期刊 |
| National Science Rev. | SCI Q1 | 卓越期刊 |
| FESE | SCI Q2 | 卓越期刊 |
| J. Geog. Sci. | SCI Q2 | 卓越期刊 |

## Submission Prediction Model

### Desk Reject Probability Factors
1. Scope mismatch (>30% contribution)
2. Poor language quality
3. Incomplete manuscript structure
4. Low novelty/contribution
5. Incorrect formatting
6. Ethical issues (no IRB, no data availability)

### Accept Probability Factors
1. Novel methodology (+15%)
2. Robust validation (+10%)
3. Clear contribution (+15%)
4. High-quality figures (+10%)
5. Comprehensive analysis (+10%)
6. Good English (+5%)
7. Proper citations (+5%)
8. Appropriate journal scope (+15%)
9. Novel dataset (+10%)
10. Reproducible code (+5%)

### Journal Recommendation Algorithm
```python
def recommend_journal(paper_topic, methods, impact_target, timeline):
    """Recommend suitable journals."""
    journals = {
        'remote_sensing_application': {
            'high': ['RSE', 'ISPRS JPRS', 'IJAEOG'],
            'medium': ['Remote Sensing', 'Ecological Indicators'],
            'low': ['JSTARS', 'IEEE GRSL']
        },
        'deep_learning_method': {
            'high': ['IEEE TGRS', 'ISPRS JPRS', 'RSE'],
            'medium': ['IJAEOG', 'JAG'],
            'low': ['IEEE GRSL', 'JSTARS']
        },
        'land_use_cover': {
            'high': ['RSE', 'ISPRS JPRS', 'IJAEOG'],
            'medium': ['Remote Sensing', 'Land', 'Ecological Indicators'],
            'low': ['JSTARS', 'GIScience']
        },
        'climate_change': {
            'high': ['Nature Climate', 'RSE', 'STOTEN'],
            'medium': ['Ecological Indicators', 'J. Cleaner Prod.'],
            'low': ['Remote Sensing', 'Atmosphere']
        },
        'urban_environment': {
            'high': ['RSE', 'STOTEN', 'ISPRS JPRS'],
            'medium': ['Remote Sensing', 'Ecological Indicators', 'Land'],
            'low': ['JSTARS', 'IEEE GRSL']
        },
        'ecosystem_service': {
            'high': ['Science Advances', 'Nature Sust.', 'RSE'],
            'medium': ['Ecological Indicators', 'Ecosystem Services'],
            'low': ['Remote Sensing', 'Land']
        }
    }
    return journals.get(paper_topic, {})
```

## Cover Letter Template
```markdown
Dear Editor,

We submit our manuscript entitled "[TITLE]" for consideration
in [JOURNAL NAME].

This study presents [KEY NOVELTY/MAIN FINDING] using
[METHODS/DATA]. The main contributions are:
1. [Contribution 1]
2. [Contribution 2]
3. [Contribution 3]

We believe our findings will interest the broad readership
of [JOURNAL NAME] because [SIGNIFICANCE].

We confirm that:
- This work has not been published elsewhere
- No conflicts of interest
- All authors have approved the submission

Thank you for your consideration.

Sincerely,

[Author Name]
[Affiliation]
[Email]
```

## Reviewer Response Template
```markdown
## Response to Reviewer [Number]

We thank the reviewer for the constructive comments.

### Comment 1:
[Reviewer comment]

**Response:**
[Detailed response]

**Changes made:** [Description of revisions, line numbers]

---

### Comment 2:
...

---

**Summary of Changes:**
- Added [X] new references
- Revised [Y] sections
- Added [Z] supplementary figures
- Updated all figures per comments
```

## Common Latex Templates Location
```
Nature:     https://www.nature.com/nature/for-authors/formatting-guide
Science:    https://www.science.org/content/page/science-information-authors
RSE:        https://www.elsevier.com/journals/remote-sensing-of-environment/0034-4257/guide-for-authors
ISPRS:      https://www.elsevier.com/journals/isprs-journal-of-photogrammetry-and-remote-sensing/0924-2716/guide-for-authors
MDPI:       https://www.mdpi.com/authors/latex
IEEE:       https://ieeeauthorcenter.ieee.org/create-your-article/ieee-companion-guide-to-latex/
Elsevier:   https://www.elsevier.com/authors/tools-and-resources/document-templates
```
