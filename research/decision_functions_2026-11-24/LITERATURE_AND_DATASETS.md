# Primary literature and general-corpus register

Prepared 2026-11-24 from primary papers and official release documentation. This is a focused starting register, not an exhaustive systematic review. Dataset descriptions below are documented properties; the execution agent must measure the actual downloaded revision. No corpus training results were produced while preparing this plan.

## Modeling foundations

| ID | Primary source | Relevance and evidence boundary |
|---|---|---|
| L1 | Garnelo et al. (ICML 2018), [Conditional Neural Processes](https://proceedings.mlr.press/v80/garnelo18a.html) | Learns predictions for a function from a support set across a distribution of functions. Our decision-maker histories are an application of that general formulation; the original experiments are not a validation of scholar prediction. |
| L2 | Deng et al. (Findings EMNLP 2023), [You Are What You Annotate](https://aclanthology.org/2023.findings-emnlp.832/) | Direct modeling of individual annotator judgments using representations of annotators/annotations; introduces TID-8. A known-person embedding and history-based adaptation to a new person must be evaluated separately. |
| L3 | Chen et al. (ICLR 2025), [PAL: Sample-Efficient Personalized Reward Modeling for Pluralistic Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/hash/2858f8c8683aaa8c12d487354cf328dc-Abstract-Conference.html) | Shared representations and compact personal parameters, including variants on frozen features. Its text summarization setting includes engineered long/short preferences; those results do not by themselves demonstrate recovery of rich individual reasoning. See [full paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/2858f8c8683aaa8c12d487354cf328dc-Paper-Conference.pdf). |
| L4 | Shenfeld et al. (2025), [Language Model Personalization via Reward Factorization](https://arxiv.org/abs/2503.06358) | Represents personal rewards through shared basis functions and individual coefficients. The [full text](https://arxiv.org/html/2503.06358v1) explains that its PRISM experiment adds synthetic cross-user annotations to address insufficient overlap. Preserve that distinction from original human observations and from the paper's separate human evaluation. |
| L5 | Poddar et al. (NeurIPS 2024), [Personalizing Reinforcement Learning from Human Feedback with Variational Preference Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5e1c255653eb98cef13f45b2d337c882-Abstract-Conference.html) | Infers a user-specific latent preference distribution. Motivates uncertainty about an individual function and informative support acquisition; no guarantee that a fixed number of observations identifies an arbitrary person's function. |
| L6 | Zhao et al. (ICLR 2024), [Group Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ffd4f5a2ea6b93e9bf5af9264d568cf2-Abstract-Conference.html) | A separately trained transformer predicts preferences from a few examples. Evaluates group and individual settings; group distributions must not be described as individual response histories. |
| L7 | Chen et al. (2026), [Human Label Variation as Stable Signal](https://arxiv.org/abs/2605.28802) | Studies individual label/explanation behavior on two sentence-pair tasks with four annotators each. Useful for a later explanation study; attribution of explanation style does not substitute for forward decision prediction. |
| L8 | Reimers and Gurevych (EMNLP-IJCNLP 2019), [Sentence-BERT](https://aclanthology.org/D19-1410/) | Explicit training of sentence representations for similarity operations. Hidden features from a language model do not automatically establish a suitable metric for our target. |
| L9 | Muennighoff et al. (EACL 2023), [MTEB](https://aclanthology.org/2023.eacl-main.148/) | Evaluates embedding methods across tasks. A representation diagnostic, not evidence that a model predicts individuals from histories. |
| L10 | Tafjord et al. (Findings ACL-IJCNLP 2021), [ProofWriter](https://aclanthology.org/2021.findings-acl.317/) | Controlled natural-language rules, implications and proofs. A future multi-rule-policy adaptation would be our new benchmark construction, not an existing human personal-decision dataset. |

## Human decision datasets

### D1 — DICES350: first pilot

- [Official repository](https://github.com/google-research-datasets/dices-dataset)
- [Official TFDS schema](https://www.tensorflow.org/datasets/catalog/dices)
- Aroyo et al., [NeurIPS 2023 dataset paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a74b697bce4cac6c91896372abaa8863-Abstract-Datasets_and_Benchmarks.html)

Documented structure: 123 raters each evaluate 350 conversations, giving 43,050 records before quality exclusions. TFDS supplies one train split; construct the person/question protocol ourselves. The schema exposes `rater_id`, `item_id`, `context`, assessed chatbot `response`, and three-class `Q_overall`. `response` is not the human outcome. The documentation lists about 29.70 MiB download for this configuration; measure actual transfer.

The dense assignment makes controlled sparsification and few-shot tests straightforward. Follow author-documented quality evidence. It is one conversational-assessment domain with 350 distinct items, not tens of thousands of independent problems. Verify source class names rather than guessing numeric codes. Source repository specifies CC BY 4.0; retain attribution and record the downloaded revision.

### D2 — MultiPref: contingency audit and candidate-choice replication

- Miranda et al., [Hybrid Preferences, ACL 2025](https://aclanthology.org/2025.acl-long.355/)
- [Official dataset card and field definitions](https://huggingface.co/datasets/allenai/multipref/blob/main/README.md)

The `default` configuration contains 10,461 response comparisons with two ordinary and two expert annotations per comparison. Individual `evaluator` identifiers, five-level preferences including ties, and reasons are retained. Group by `prompt_id`, then comparison identity; inspect per-person histories and expert/topic routing.

`human_overall_binarized` aggregates preferences and randomly resolves some ties, so it is unsuitable for the individual-function target. Reasons, confidence and timing for the query belong to evaluator evidence. Keep the actual candidate texts in the predictor. The card lists ODC-BY; audit the acquisition revision and distribution terms. Density and overlap must be measured before committing to a support-size curve.

### D3 — TID-8 CommitmentBank: semantic-inference replication

- L2 above
- [Official TID-8 release](https://huggingface.co/datasets/MichiganNLP/TID-8)

The release includes `question`, `uid`, `annotator_id`, `answer`, `answer_label`, and `weak_labels`. It offers annotation splits retaining the same people and annotator splits holding people out. Both still need a history/query design and item-family audit for our study. `answer_label` is a category index; recover the true ordered judgment values from the declared mapping before using ordinal losses. `weak_labels` contains other judgments and is excluded from unseen-query prediction. The top-level card lists an unknown license; record the underlying constituent terms before redistribution.

### D4 — LeWiDi / VariErr / Par: labels and reasons

- [LeWiDi 2025 task paper](https://aclanthology.org/2025.nlperspectives-1.16/)
- [Updated full task paper](https://aclanthology.org/2025.nlperspectives-1.16v3.pdf)
- [VariErr NLI, ACL 2024](https://aclanthology.org/2024.acl-long.123/)

LeWiDi includes prediction of individual annotator labels. VariErr reannotates 500 MNLI items with four annotators and explanations; its first-round labels can be multiple accepted categories. Par supplies paraphrase ratings and explanations with four annotators. This is useful for substantive interpretation but small for a broad new-person claim. Keep valid disagreement distinct from annotation error, and do not assume annotator IDs link across tasks without verification.

### D5 — PRISM / PersonalRewardBench: realistic sparse histories

- [PRISM paper](https://arxiv.org/abs/2404.16019)
- [Official PRISM data](https://huggingface.co/datasets/HannahRoseKirk/prism-alignment)
- Ryan et al., [SynthesizeMe / PersonalRewardBench, ACL 2025](https://aclanthology.org/2025.acl-long.397/)

PRISM preserves user-linked conversations and ratings. PersonalRewardBench curates personal preference histories from PRISM and Chatbot Arena, with 854 users in total. Such choices can reflect presentation, length and usefulness as well as substantive conclusions. Audit the exact identity proxy, selection filters, and conversation overlap; do not treat a curated derivative as an independent human population. The PRISM portion is a useful later sparse-history check. Model-generated persona descriptions are not observed human reasoning.

### D6 — Surveys: broader question–answer matrices

- Zhao et al., [WorldValuesBench, LREC-COLING 2024](https://aclanthology.org/2024.lrec-main.1539/)
- [Official construction repository](https://github.com/Demon702/WorldValuesBench)
- Santurkar et al., [Whose Opinions Do Language Models Reflect?, ICML 2023](https://proceedings.mlr.press/v202/santurkar23a.html)
- [Official OpinionQA release](https://github.com/tatsu-lab/opinions_qa)

WorldValuesBench construction retains respondent-level answers, while the published evaluation emphasizes demographic contexts and distributions. Original WVS acquisition is separate from the code repository. OpinionQA also releases individual human responses; it is not aggregate-only. Before using either for our objective, inspect the actual ID scope, wave structure, available history per respondent, and response codes. Do not assume cross-wave personal continuity. Matching aggregate answer distributions cannot establish correct individual predictions.

## Synthetic and encoder resources

### D7 — PersonalLLM

- Zollo et al., [PersonalLLM, ICLR 2025](https://arxiv.org/html/2409.20296v2)
- [Dataset](https://huggingface.co/datasets/namkoong-lab/PersonalLLM)
- [Evaluation data](https://huggingface.co/datasets/namkoong-lab/PersonalLLM_Eval)

Simulates users through weighted combinations of pretrained reward models over generated alternatives. Useful for known-function engineering and controlled sparsity, with separate human validation needed. Do not give the learner hidden `person_weight`, query rewards or best-answer targets. A factorized predictor may be favored by the simulator's own construction; include a misspecified synthetic regime before making general claims.

### E1 — Compact frozen encoder for the first pilot

- [Official all-MiniLM-L6-v2 model card](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

This is a practical small baseline, not a claim of current best embedding performance. The executing agent resolves an immutable checkpoint revision and records the pooling, tokenizer, maximum length and license. Our full-input window aggregation is an explicitly proposed adaptation whose decision sensitivity remains to be tested.

## Source-use rules for reporting

Use original papers and official release documentation for factual claims. Separate a paper's reported result from this project's proposal or measurement. Do not transfer headline sample-efficiency gains to another domain. Preserve synthetic-versus-human provenance, group-versus-person distinctions, and known-item-versus-new-item evaluation scope. Include direct source URLs and immutable data/model revisions in the executed reports.
