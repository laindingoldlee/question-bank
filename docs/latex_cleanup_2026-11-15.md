# LaTeX clean-up, 2026-11-15

Every question and solution (64,424 bodies) was checked three ways:

1. **pdflatex**: all bodies compiled in chunks (`tools/checks/compile_check.py`). Before: 4 questions with errors. After: 0.
2. **Lint** for house rules and math/text mix-ups (`tools/checks/lint.py`): non-ASCII, `\frac`, slash fractions, maths commands outside `$...$`.
3. **Website display audit**: every body rendered with the site's renderer and MathJax in headless Chrome (`tools/checks/display_audit.py`). After: 0 bodies with raw LaTeX showing (one intentional `\verb` example excepted).

Most display problems were bugs in the website's renderer (escaped `\$` treated as a maths delimiter; text macros not processed inside lists), fixed in `site/index.html`.

## Mechanical source changes

276 files changed:

- Non-ASCII characters replaced with LaTeX equivalents: 260 files
- Text-mode \boxed wrapped in $...$: 37 files
- \frac changed to \dfrac: 2 files

## Hand fixes

- `aops-topic-3535283-q01` solution.tex: math written outside $...$ (A_i, digits)
- `aops-topic-3167360-q04` solution.tex: math written outside $...$
- `aops-topic-3129723-q08` solution.tex: fraction outside $...$
- `aops-topic-3375917-q01` question.tex: blank written as ___ (subscripts); unclosed quotation
- `aops-3644113-q25` question.tex: non-ASCII times sign
- `aops-h3858066-q01` question.tex: forum chatter removed; non-ASCII times sign
- `aops-3134489-q31` question.tex: product written as plain text with non-ASCII dots
- `aops-3765589` question.tex: degree sign outside math
- `aops-topic-2817080-q01` solution.tex: slash fraction -> \dfrac (x1)
- `aops-topic-2827341-q01` solution.tex: slash fraction -> \dfrac (x1)
- `aops-h3748893-q01` solution.tex: slash fraction -> \dfrac (x1)
- `aops-topic-2812794-q01` solution.tex: slash fraction -> \dfrac (x1)
- `aops-h3852226-q01` question.tex: \emph placed inside $...$
- `aops-h3894749-q01` solution.tex: \textquotesingle inside math -> prime

## Mechanical change list

| Question | File | Changes |
|---|---|---|
| `aops-topic-3539965-q01` | question.tex | non-ASCII '–' -> -- |
| `aops-topic-3252461-q02` | question.tex | non-ASCII '’' -> ' |
| `aops-3644927-b21` | question.tex | non-ASCII '’' -> ' |
| `aops-3767437` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3042250-q01` | solution.tex | non-ASCII '–' -> -- |
| `aops-3644927-b25` | question.tex | non-ASCII '’' -> ' |
| `aops-3678684-q03` | question.tex | non-ASCII '’' -> ' |
| `aops-3651287-q08` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2786721-q12` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2766233-q13` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3054751-q11` | solution.tex | non-ASCII '’' -> ' |
| `aops-3644931-w12` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-1665297-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-1844155-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-3054751-q19` | solution.tex | non-ASCII '–' -> -- |
| `aops-topic-3129723-q02` | solution.tex | non-ASCII '–' -> -- |
| `aops-3653445-q18` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-topic-1949018-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-2779431-q02` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2779431-q02` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3262094-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-1782319-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-3642631-q06` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3054751-q03` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3092533-q02` | question.tex | non-ASCII '’' -> ' |
| `aops-3639111-q03` | question.tex | non-ASCII '’' -> ' |
| `aops-3639111-q03` | solution.tex | non-ASCII '’' -> ' |
| `aops-3647494-q17` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3131523-q08` | solution.tex | non-ASCII '’' -> ' |
| `aops-h3831926-q01` | question.tex | non-ASCII '…' -> \ldots{} |
| `aops-topic-3182830-q13` | question.tex | non-ASCII '’' -> ' |
| `aops-3642631-q04` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3045186-q02` | solution.tex | non-ASCII '–' -> -- |
| `aops-3648502-q14` | question.tex | non-ASCII '’' -> ' |
| `aops-3641052-q04` | question.tex | non-ASCII '’' -> ' |
| `aops-3640968-q06` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-3644113-q15` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3038731-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3038731-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-1946190-q02` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-2766233-q06` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2934024-q08` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3050540-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3050540-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3093587-q10` | question.tex | non-ASCII '’' -> ' |
| `aops-3644044-q04` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3133709-q15` | solution.tex | non-ASCII '–' -> -- |
| `aops-topic-3133709-q17` | solution.tex | non-ASCII '’' -> ' |
| `aops-3644032-w14` | question.tex | non-ASCII '’' -> ' |
| `aops-3644375-r3q2` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2582276-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-1926198-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-2915810-q14` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2915810-q14` | solution.tex | non-ASCII '’' -> ' |
| `aops-3642477-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3132167-q13` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-1657159-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-3644113-q16` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3054751-q21` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3051229-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-3642473-q02` | question.tex | non-ASCII '’' -> ' |
| `aops-3647131-q06` | question.tex | non-ASCII '’' -> ' |
| `aops-3642477-q04` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-h3747395-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-3644939-q18` | question.tex | non-ASCII '’' -> '; non-ASCII '‘' -> `; non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-3646513-q07` | question.tex | non-ASCII '’' -> ' |
| `aops-3642645-q03` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-1656531-q15` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-3098388-q01` | solution.tex | non-ASCII '–' -> -- |
| `aops-3166476-q18` | question.tex | non-ASCII '’' -> ' |
| `aops-3642053-q09` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-topic-2765486-q18` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3092776-q01` | solution.tex | non-ASCII '–' -> -- |
| `aops-topic-3049712-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-3644931-e30` | question.tex | non-ASCII '’' -> ' |
| `aops-3773311` | question.tex | non-ASCII '’' -> ' |
| `aops-3642473-q04` | question.tex | non-ASCII '’' -> ' |
| `aops-3642473-q04` | solution.tex | non-ASCII '’' -> ' |
| `aops-3644927-b29` | question.tex | non-ASCII '’' -> ' |
| `aops-3648502-q02` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-1664848-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-2945150-q04` | solution.tex | non-ASCII '–' -> -- |
| `aops-2523963` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-3258995-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3129226-q03` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3131523-q06` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-1657646-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-3123660-q01` | solution.tex | non-ASCII '–' -> -- |
| `aops-3640986-r5q3` | solution.tex | non-ASCII '’' -> ' |
| `aops-3642473-q07` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-1658301-q02` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-2915810-q22` | solution.tex | non-ASCII '’' -> ' |
| `aops-3640976-r3q3` | solution.tex | non-ASCII 'ö' -> \"o |
| `aops-topic-2581581-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-3644113-q17` | solution.tex | non-ASCII '’' -> '; non-ASCII 'é' -> \'e |
| `aops-3644927-b26` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-1947927-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-3181320-q09` | question.tex | non-ASCII '’' -> ' |
| `aops-3678803-q10` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3179900-q07` | solution.tex | non-ASCII '–' -> -- |
| `aops-3644032-e10` | question.tex | non-ASCII '’' -> ' |
| `aops-3678829-q05` | question.tex | non-ASCII '’' -> ' |
| `aops-3642629-q02` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-3642629-q02` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3096514-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3262759-q03` | question.tex | non-ASCII '’' -> ' |
| `aops-3647999-q03` | question.tex | non-ASCII '’' -> ' |
| `aops-3640968-q05` | question.tex | non-ASCII '’' -> '; non-ASCII '”' -> '' |
| `aops-3640968-q05` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3094898-q12` | solution.tex | non-ASCII '–' -> -- |
| `aops-topic-2388517-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-3035600-q07` | solution.tex | non-ASCII '’' -> ' |
| `aops-3644044-q22` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3158461-q01` | question.tex | non-ASCII '–' -> -- |
| `aops-topic-2765486-q13` | question.tex | non-ASCII '’' -> ' |
| `aops-3642629-q05` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-2778565-q03` | question.tex | non-ASCII '’' -> ' |
| `aops-3646489-q14` | question.tex | non-ASCII '’' -> ' |
| `aops-3678677-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2160076-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-3644931-w23` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3046964-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3186838-q11` | question.tex | non-ASCII '’' -> ' |
| `aops-3644330-r3q2` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-1656531-q19` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-2793860-q13` | solution.tex | non-ASCII '–' -> -- |
| `aops-3643910-q19` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-1636407-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-2934024-q11` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3094162-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3094162-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-h3776613-p08` | solution.tex | non-ASCII '–' -> -- |
| `aops-topic-2916240-q04` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2916240-q03` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3248729-q10` | solution.tex | non-ASCII '’' -> ' |
| `aops-3678829-q04` | question.tex | non-ASCII '’' -> ' |
| `aops-3641088-q06` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2915810-q16` | solution.tex | non-ASCII '–' -> -- |
| `aops-topic-3054751-q14` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3040268-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-3641990-q13` | question.tex | non-ASCII '’' -> ' |
| `aops-h3798612-p09` | question.tex | non-ASCII '—' -> --- |
| `aops-topic-2778565-q17` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-1569700-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-3641052-q05` | question.tex | non-ASCII '’' -> ' |
| `aops-3766713` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-3641990-q14` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-2530369-q06` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-3129723-q09` | solution.tex | non-ASCII '–' -> -- |
| `aops-3641996-q03` | question.tex | non-ASCII '’' -> ' |
| `aops-3678677-q12` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3098107-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-1662703-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-2779997-q09` | solution.tex | non-ASCII '–' -> -- |
| `aops-topic-1912412-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-3647999-q04` | question.tex | non-ASCII '’' -> ' |
| `aops-3648502-q05` | question.tex | non-ASCII '’' -> ' |
| `aops-3721582` | question.tex | non-ASCII '’' -> ' |
| `aops-3647482-q07` | question.tex | non-ASCII '’' -> ' |
| `aops-3643910-q12` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-1659439-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-2915803-q10` | question.tex | non-ASCII '’' -> ' |
| `aops-3678660-q09` | question.tex | non-ASCII '—' -> --- |
| `aops-3644930-e9` | question.tex | non-ASCII '’' -> ' |
| `aops-3644930-e15` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3133709-q19` | solution.tex | non-ASCII '’' -> ' |
| `aops-3642005-q14` | question.tex | non-ASCII '’' -> ' |
| `aops-3642005-q14` | solution.tex | non-ASCII '’' -> ' |
| `aops-3640968-q10` | solution.tex | non-ASCII 'ö' -> \"o |
| `aops-3644032-e7` | question.tex | non-ASCII '’' -> ' |
| `aops-3644032-e7` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3099069-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3132170-q05` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-h3857678-p15` | question.tex | non-ASCII 'ş' -> \c{s} |
| `aops-topic-3035600-q14` | solution.tex | non-ASCII '–' -> -- |
| `aops-topic-3166019-q24` | solution.tex | non-ASCII '–' -> -- |
| `aops-3642473-q06` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-3678803-q06` | question.tex | non-ASCII '–' -> -- |
| `aops-topic-3131590-q21` | solution.tex | non-ASCII 'ü' -> \"u |
| `aops-topic-3035600-q11` | solution.tex | non-ASCII '–' -> -- |
| `aops-topic-2779431-q113` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3132167-q02` | question.tex | non-ASCII '’' -> ' |
| `aops-h1933900-q01` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-3642629-q04` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3181320-q02` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-topic-2778565-q13` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3045506-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-3642629-q06` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2782134-q14` | solution.tex | non-ASCII '–' -> -- |
| `aops-topic-250972-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-1948212-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-3181929-q11` | question.tex | non-ASCII '–' -> -- |
| `aops-3648493-q06` | question.tex | non-ASCII '’' -> ' |
| `aops-3777490-q28` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-topic-2952214-q03` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3136014-q22` | solution.tex | non-ASCII '’' -> ' |
| `aops-3644012-e2` | question.tex | non-ASCII '’' -> ' |
| `aops-3678829-q03` | question.tex | non-ASCII '’' -> ' |
| `aops-3644330-r1q1` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3038898-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-3644001-q03` | question.tex | non-ASCII '’' -> ' |
| `aops-3648502-q20` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3092533-q05` | solution.tex | non-ASCII '’' -> ' |
| `aops-3644383-r6q3` | question.tex | non-ASCII '”' -> '' |
| `aops-topic-3049053-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3181951-q10` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-1942860-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-3644330-r2q3` | question.tex | non-ASCII '’' -> ' |
| `aops-3644044-q25` | question.tex | non-ASCII '’' -> ' |
| `aops-3774418-q25` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-topic-1637394-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-3642473-q01` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-topic-3045506-q02` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-topic-3045506-q02` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3054751-q08` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3093295-q02` | solution.tex | non-ASCII '–' -> -- |
| `aops-3644939-q11` | question.tex | non-ASCII '’' -> '; non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-3644939-q11` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-2160682-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-3640968-q09` | solution.tex | non-ASCII '’' -> ' |
| `aops-3643910-q17` | question.tex | non-ASCII '’' -> ' |
| `aops-h2790248-p02` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3098230-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2778565-q06` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3298491-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3298491-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-2766233-q10` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2766233-q10` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-2920216-q02` | solution.tex | \frac -> \dfrac |
| `aops-3678660-q11` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2155063-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-3094898-q10` | question.tex | non-ASCII '’' -> ' |
| `aops-3678803-q11` | question.tex | non-ASCII '’' -> ' |
| `aops-3644923-b15` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2766233-q07` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3052680-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3052680-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3133709-q16` | solution.tex | non-ASCII '’' -> ' |
| `aops-3644113-q20` | question.tex | non-ASCII '’' -> ' |
| `aops-h3768248-p24` | question.tex | non-ASCII '—' -> --- |
| `aops-topic-2580164-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-3641052-q02` | question.tex | non-ASCII '’' -> ' |
| `aops-3644930-e10` | question.tex | non-ASCII '’' -> ' |
| `aops-3763363-q15` | question.tex | non-ASCII '—' -> --- |
| `aops-topic-1429842-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x2) |
| `aops-topic-1656531-q16` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-3272064-q08` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3303471-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-1637787-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-2026245-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-2025485-q02` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-3131523-q07` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-1634220-q01` | solution.tex | text-mode \boxed wrapped in $...$ (x1) |
| `aops-topic-2916250-q27` | solution.tex | \frac -> \dfrac |
| `aops-topic-3129226-q05` | question.tex | non-ASCII '’' -> ' |
| `aops-3646502-q11` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-3646502-q12` | question.tex | non-ASCII '’' -> ' |
| `aops-3642477-q05` | solution.tex | non-ASCII '’' -> ' |
| `aops-3646513-q13` | question.tex | non-ASCII '’' -> ' |
| `aops-3648502-q15` | question.tex | non-ASCII '’' -> ' |
| `aops-3641990-q04` | question.tex | non-ASCII '’' -> ' |
| `aops-3646502-q15` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-2765486-q09` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3046461-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-2779451-q10` | question.tex | non-ASCII '’' -> '; non-ASCII '–' -> -- |
| `aops-topic-2779451-q10` | solution.tex | non-ASCII '’' -> ' |
| `aops-topic-3047011-q01` | solution.tex | non-ASCII '–' -> -- |
| `aops-topic-3043163-q01` | question.tex | non-ASCII '’' -> ' |
| `aops-topic-3043163-q01` | solution.tex | non-ASCII '’' -> ' |
| `aops-3641088-q08` | question.tex | non-ASCII '’' -> ' |
| `aops-3641088-q08` | solution.tex | non-ASCII '’' -> ' |
| `aops-3640986-r8q2` | question.tex | non-ASCII '“' -> ``; non-ASCII '”' -> '' |
| `aops-3166476-q13` | question.tex | non-ASCII '’' -> ' |
| `aops-3648502-q19` | question.tex | non-ASCII '’' -> ' |
| `aops-3644001-q14` | question.tex | non-ASCII '’' -> ' |
| `aops-3644927-b19` | question.tex | non-ASCII '’' -> ' |
