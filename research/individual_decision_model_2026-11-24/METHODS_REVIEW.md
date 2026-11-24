# Reference-method review — 2026-11-24

Independent AI review, not experimental replication or knowledgeable-human review. Paper versions and observed repository HEADs are pinned in `references_manifest.json`; HEAD observation does not establish that a repository exactly reproduces the cited paper version. No implementation was executed. Shared latent profiles, reward factorization, and adaptive questionnaires are established methods; this pilot tests their usefulness under narrower access controls.

## PReF

[PReF v1](https://arxiv.org/html/2503.06358v1) factorizes personal rewards into shared basis functions and user coefficients under pairwise Bradley–Terry preferences. Evaluation separates prompts and users; calibration infers new-user coefficients. Attributes uses synthetic users; PRISM is augmented with synthetic preference annotations to obtain overlap. The human study is response personalization, not cross-task psychological-choice transfer. Its headline win rate is therefore not this pilot's estimand. The Hessian-based query mechanism motivates uncertainty-aware elicitation, but is not an exact Bayesian posterior. [Code](https://github.com/idanshen/PReF_code) exposes feature training and user discovery; `discover_user.py` was inspected. A small Gaussian MAP/Laplace model is an adaptation, not a reproduction.

## Variational Preference Learning

[VPL v1](https://arxiv.org/html/2408.10075v1) infers latent context from preference comparisons and conditions reward/policy prediction on it. Control experiments and active preference querying are distinct from the language experiments. Pets is synthetic; UltraFeedback-P creates user types from attribute scores, including divergent-comparison filtering. These are not large samples of independent linked human decision makers. The paper's context-noise experiment concerns new preferences resembling training types. [LLM implementation](https://github.com/WEIRDLabUW/vpl_llm) contains pair/sequence encoders, a VAE decoder, and KL-weighted training in inspected `hidden_context/vae_utils.py`. The [control repository](https://github.com/WEIRDLabUW/vpl) was located and its tree pinned, not run. Approximate latent uncertainty is relevant, but its published accuracy is not evidence that eight human source decisions transfer between our proposed tasks.

## Adaptive Querying with AI Persona Priors

The [PMLR paper](https://proceedings.mlr.press/v306/wang26jb.html), with [v2 full text](https://arxiv.org/html/2605.00696v2), uses a finite persona dictionary with categorical response distributions and Bayesian mixture updates. Scope: synthetic data and WorldValuesBench survey answers, not sequential reward-learning trials. The [released code](https://github.com/yw3453/adaptive-query-ai-persona-priors) supplies greedy, nonadaptive and random policies. Inspected `src/greedy.py` normalizes likelihood-weighted persona probabilities and computes expected target cost over possible answers. The README distinguishes shipped simulated persona answers from real WVS data that require separate access. This supports later offline selection comparisons; it does not authorize fabricating human answers or equating a generated persona with a verified psychological individual.

## Cross-Centaur and Cross-Psych

[Authoritative ACL paper](https://aclanthology.org/2026.emnlp-main.2235.pdf): source-task transcripts condition target behavior. Participant-held-out evaluation uses an 80/20 split; separate task-held-out experiments remove that task from both source and target training. Action-token modeling is not automatically normalized complete-alternative loss.

Sections 4–5 and footnote 3 distinguish 601 experiment participants from 591 public-release participants after ten opt-outs; 261,551 released valid decisions differs from 273,343 initially recorded decisions. Figure 8 uses 601. This is critical release provenance, not a harmless interchangeable count. The paper's main experiment uses the full 601.

No raw-task repository was located through the paper (no GitHub link in extracted PDF). Table 5 and interface screenshots describe tasks but do not replace executable task sequencing. Bandits, classification learning, and card continuation cannot be assumed static. Temporal discounting and one-shot gamble require raw definition checks before admission. Any released 601-person cohort conflicts with the described opt-out release and must be resolved before use.

The [HF release](https://huggingface.co/datasets/HikaruAsano/cross-psych-101/tree/532794c51e046a0ddaf560e7972789688d46bf63) contains only metadata and two parquets. Its raw 656-byte README has schema/split metadata, no license or use grant. API confirms 29,118/7,295 transcript rows; these are not independent choices. Absence of a stated license is an admission gap, not proof of a restrictive license. No claim is made that code or permission cannot exist elsewhere.

## PLUS

[PLUS v4](https://arxiv.org/html/2507.13579v4) jointly trains a text summarizer and personalized reward model through co-adaptation. Evaluation includes constructed Pets/UltraFeedback preferences, a Pets preference shift, and PRISM user/conversation holdouts. Text summaries and useful latent representations are existing prior work, not inventions of this pilot. Summaries can incorporate richer context than a bounded decision history: a fair baseline here must use only the same revealed decisions. [Released implementation](https://github.com/nam630/pluralistic_user_summary_public) extends OpenRLHF; its README specifies separate context, summarizer-training, reward-training and evaluation fields. Inspected `personalized_dataset.py` establishes a released data-loader entry point, not certification of every training boundary. GPU-scale reported training is outside this CPU pilot. Pinning v4 matters because earlier versions need not share its evaluation scope.

## Individuality transfer

The [eLife Version of Record](https://doi.org/10.7554/eLife.107163.3), also [archived in PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12815462/), learns an encoder, individual representation, decoder and task solver. A decoder generates solver weights. Tests include unseen participants and comparison with other people's solvers. Transfer is between task conditions, separately demonstrated in value-guided and perceptual settings; it is not evidence for one universal cross-domain psychological signature. [Code/data](https://github.com/hgshrs/indiv_trans) are released. Inspected `train_it_mdp.py` splits participant IDs and implements recurrent encoders, generated weights and sequence processing. This is close precedent for own-versus-other evidence, but its hypernetwork and sequential environments are unnecessary complexity for the present static pilot.

## Implications for this pilot

The defensible claim is predictive individual information in a fixed task pair, conditional on training people and allowed source observations. Population and source-summary comparisons are necessary alongside matched other-person controls. A positive result is not proof of an identifiable trait, causal psychological mechanism, live adaptive effectiveness, or general transfer to unseen task families. Complete-alternative probabilities, participant-cluster uncertainty, source-only inference and canonical-decision deduplication remain requirements regardless of published benchmark conventions.

Resource note: direct HTTP body bytes are counted in the manifest, including metadata and inspected code; web-tool transfer bytes are unavailable. No dataset/model downloads or training were performed by this reviewer.
