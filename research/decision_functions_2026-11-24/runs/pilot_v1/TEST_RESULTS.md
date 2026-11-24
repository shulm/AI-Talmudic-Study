# Test results

```json
{
  "status": "VALID_PILOT_POSITIVE_PRIMARY",
  "freeze_commit": "4de12a1fb300a7c9e9d927591bc4b101f0e263a2",
  "split": "test",
  "people": 22,
  "items": 76,
  "groups": 55,
  "disagreement_items": 69,
  "primary_baseline": "B3",
  "primary": {
    "delta": 1.9145913755253597e-12,
    "interval95": [
      1.655029168969052e-13,
      3.804900589608094e-12
    ],
    "valid_resamples": 2000,
    "rejected": 0
  },
  "contrasts": {
    "B2": {
      "delta": 0.052063435022851594,
      "interval95": [
        0.014072400815651859,
        0.09861916330252561
      ],
      "valid_resamples": 2000,
      "rejected": 0
    },
    "B3": {
      "delta": 1.9145913755253597e-12,
      "interval95": [
        1.655029168969052e-13,
        3.804900589608094e-12
      ],
      "valid_resamples": 2000,
      "rejected": 0
    }
  },
  "support_curve": [
    {
      "model": "B0",
      "k": 0,
      "nll": 0.7829414360810504,
      "accuracy": 0.6758373205741627,
      "brier": 0.483412863425011,
      "disagreement_subset": {
        "nll": 0.7909022096718896,
        "accuracy": 0.6719367588932806,
        "brier": 0.4872222570349473
      }
    },
    {
      "model": "B0",
      "k": 4,
      "nll": 0.7829414360810504,
      "accuracy": 0.6758373205741627,
      "brier": 0.483412863425011,
      "disagreement_subset": {
        "nll": 0.7909022096718896,
        "accuracy": 0.6719367588932806,
        "brier": 0.4872222570349473
      }
    },
    {
      "model": "B0",
      "k": 16,
      "nll": 0.7829414360810504,
      "accuracy": 0.6758373205741627,
      "brier": 0.483412863425011,
      "disagreement_subset": {
        "nll": 0.7909022096718896,
        "accuracy": 0.6719367588932806,
        "brier": 0.4872222570349473
      }
    },
    {
      "model": "B0",
      "k": 64,
      "nll": 0.7829414360810504,
      "accuracy": 0.6758373205741627,
      "brier": 0.483412863425011,
      "disagreement_subset": {
        "nll": 0.7909022096718896,
        "accuracy": 0.6719367588932806,
        "brier": 0.4872222570349473
      }
    },
    {
      "model": "B1",
      "k": 0,
      "nll": 0.7829414360810504,
      "accuracy": 0.6758373205741627,
      "brier": 0.483412863425011,
      "disagreement_subset": {
        "nll": 0.7909022096718896,
        "accuracy": 0.6719367588932806,
        "brier": 0.4872222570349473
      }
    },
    {
      "model": "B1",
      "k": 4,
      "nll": 0.7782686572756307,
      "accuracy": 0.6180223285486443,
      "brier": 0.4873923961115927,
      "disagreement_subset": {
        "nll": 0.7833825921630589,
        "accuracy": 0.6194554238032499,
        "brier": 0.4876198513937815
      }
    },
    {
      "model": "B1",
      "k": 16,
      "nll": 0.7262868593407651,
      "accuracy": 0.648524720893142,
      "brier": 0.4530941391217366,
      "disagreement_subset": {
        "nll": 0.7274395878668778,
        "accuracy": 0.6490996925779534,
        "brier": 0.4516113168289999
      }
    },
    {
      "model": "B1",
      "k": 64,
      "nll": 0.6995362663325871,
      "accuracy": 0.6734449760765551,
      "brier": 0.43536652054180003,
      "disagreement_subset": {
        "nll": 0.6986459343969625,
        "accuracy": 0.6706192358366271,
        "brier": 0.4334858288432106
      }
    },
    {
      "model": "B2",
      "k": 0,
      "nll": 0.7725119731423172,
      "accuracy": 0.6758373205741627,
      "brier": 0.47470303072427616,
      "disagreement_subset": {
        "nll": 0.7826927389736346,
        "accuracy": 0.6719367588932806,
        "brier": 0.48048863162445704
      }
    },
    {
      "model": "B2",
      "k": 4,
      "nll": 0.7725119731423172,
      "accuracy": 0.6758373205741627,
      "brier": 0.47470303072427616,
      "disagreement_subset": {
        "nll": 0.7826927389736346,
        "accuracy": 0.6719367588932806,
        "brier": 0.48048863162445704
      }
    },
    {
      "model": "B2",
      "k": 16,
      "nll": 0.7725119731423172,
      "accuracy": 0.6758373205741627,
      "brier": 0.47470303072427616,
      "disagreement_subset": {
        "nll": 0.7826927389736346,
        "accuracy": 0.6719367588932806,
        "brier": 0.48048863162445704
      }
    },
    {
      "model": "B2",
      "k": 64,
      "nll": 0.7725119731423172,
      "accuracy": 0.6758373205741627,
      "brier": 0.47470303072427616,
      "disagreement_subset": {
        "nll": 0.7826927389736346,
        "accuracy": 0.6719367588932806,
        "brier": 0.48048863162445704
      }
    },
    {
      "model": "B3",
      "k": 0,
      "nll": 0.7725119731423172,
      "accuracy": 0.6758373205741627,
      "brier": 0.47470303072427616,
      "disagreement_subset": {
        "nll": 0.7826927389736346,
        "accuracy": 0.6719367588932806,
        "brier": 0.48048863162445704
      }
    },
    {
      "model": "B3",
      "k": 4,
      "nll": 0.8022081135845333,
      "accuracy": 0.6106459330143541,
      "brier": 0.499796934487789,
      "disagreement_subset": {
        "nll": 0.8057115893261457,
        "accuracy": 0.6113306982872201,
        "brier": 0.49953921168768706
      }
    },
    {
      "model": "B3",
      "k": 16,
      "nll": 0.7204485381213804,
      "accuracy": 0.6586921850079746,
      "brier": 0.4442661513358776,
      "disagreement_subset": {
        "nll": 0.72304753433734,
        "accuracy": 0.6559068950373298,
        "brier": 0.44461507487939933
      }
    },
    {
      "model": "B3",
      "k": 64,
      "nll": 0.7001304419811302,
      "accuracy": 0.6804226475279108,
      "brier": 0.4290215562173663,
      "disagreement_subset": {
        "nll": 0.7028013917930832,
        "accuracy": 0.6761089152393499,
        "brier": 0.4296114687115158
      }
    },
    {
      "model": "B4",
      "k": 0,
      "nll": 0.7725119731423172,
      "accuracy": 0.6758373205741627,
      "brier": 0.47470303072427616,
      "disagreement_subset": {
        "nll": 0.7826927389736346,
        "accuracy": 0.6719367588932806,
        "brier": 0.48048863162445704
      }
    },
    {
      "model": "B4",
      "k": 4,
      "nll": 0.7570688510819233,
      "accuracy": 0.6401515151515151,
      "brier": 0.467685870623854,
      "disagreement_subset": {
        "nll": 0.7647572289601591,
        "accuracy": 0.6383399209486166,
        "brier": 0.47070251047481165
      }
    },
    {
      "model": "B4",
      "k": 16,
      "nll": 0.7280984870479158,
      "accuracy": 0.6618819776714514,
      "brier": 0.4478937660752475,
      "disagreement_subset": {
        "nll": 0.7325312147555971,
        "accuracy": 0.6611769872639438,
        "brier": 0.44888401228326513
      }
    },
    {
      "model": "B4",
      "k": 64,
      "nll": 0.7102863079590644,
      "accuracy": 0.6790271132376396,
      "brier": 0.4337757360308007,
      "disagreement_subset": {
        "nll": 0.7203631861512036,
        "accuracy": 0.6756697408871322,
        "brier": 0.4390651674993848
      }
    },
    {
      "model": "M1",
      "k": 0,
      "nll": 0.7725119731423172,
      "accuracy": 0.6758373205741627,
      "brier": 0.47470303072427616,
      "disagreement_subset": {
        "nll": 0.7826927389736346,
        "accuracy": 0.6719367588932806,
        "brier": 0.48048863162445704
      }
    },
    {
      "model": "M1",
      "k": 4,
      "nll": 0.8022081135764507,
      "accuracy": 0.6106459330143541,
      "brier": 0.49979693448302903,
      "disagreement_subset": {
        "nll": 0.8057115893186385,
        "accuracy": 0.6113306982872201,
        "brier": 0.49953921168314425
      }
    },
    {
      "model": "M1",
      "k": 16,
      "nll": 0.7204485381194657,
      "accuracy": 0.6586921850079746,
      "brier": 0.44426615133463293,
      "disagreement_subset": {
        "nll": 0.7230475343353548,
        "accuracy": 0.6559068950373298,
        "brier": 0.44461507487807217
      }
    },
    {
      "model": "M1",
      "k": 64,
      "nll": 0.700130441979573,
      "accuracy": 0.6804226475279108,
      "brier": 0.42902155621634935,
      "disagreement_subset": {
        "nll": 0.7028013917914833,
        "accuracy": 0.6761089152393499,
        "brier": 0.4296114687104727
      }
    }
  ],
  "seed_diagnostics": [
    {
      "seed": 11,
      "nll": 0.7204485381161646
    },
    {
      "seed": 29,
      "nll": 0.7204485381212171
    },
    {
      "seed": 47,
      "nll": 0.7204485381210156
    }
  ],
  "history_controls": [
    {
      "model": "B3",
      "true_nll": 0.7204485381213804,
      "shuffled_nll": 0.8145900346846182,
      "true_history_advantage": 0.09414149656323786
    },
    {
      "model": "B4",
      "true_nll": 0.7280984870479158,
      "shuffled_nll": 0.7889511547774672,
      "true_history_advantage": 0.060852667729551495
    },
    {
      "model": "M1",
      "true_nll": 0.7204485381194657,
      "shuffled_nll": 0.8145900346844069,
      "true_history_advantage": 0.09414149656494109
    }
  ],
  "adaptation_person_solves": 3630,
  "artifacts": [
    {
      "filename": "test_predictions.npz",
      "bytes": 3583087,
      "sha256": "25b3f08b45c360483984c6ae61f2e067da466b45fcffcb13f9f7caaf5e536927"
    },
    {
      "filename": "test_paired_losses.npz",
      "bytes": 136988,
      "sha256": "a4b5d74830f816ec83224ea5f77ef5f4bbd899f2c25bad58efcfe7340f06ae83"
    }
  ]
}
```
