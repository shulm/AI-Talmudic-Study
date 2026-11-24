# Development results

```json
{
  "status": "DEVELOPMENT_DIAGNOSTIC",
  "freeze_commit": null,
  "split": "development",
  "people": 20,
  "items": 67,
  "groups": 54,
  "disagreement_items": 67,
  "primary_baseline": "B3",
  "primary": {
    "delta": 9.84061868061977e-13,
    "interval95": [
      -5.277302042189814e-13,
      2.3961912968853435e-12
    ],
    "valid_resamples": 2000,
    "rejected": 0
  },
  "contrasts": {
    "B3": {
      "delta": 9.84061868061977e-13,
      "interval95": [
        -5.277302042189814e-13,
        2.3961912968853435e-12
      ],
      "valid_resamples": 2000,
      "rejected": 0
    },
    "B2": {
      "delta": 0.09409939224196702,
      "interval95": [
        0.03468157767679766,
        0.15432712000840848
      ],
      "valid_resamples": 2000,
      "rejected": 0
    }
  },
  "support_curve": [
    {
      "model": "B0",
      "k": 0,
      "nll": 0.8085730386845184,
      "accuracy": 0.6656716417910448,
      "brier": 0.4951459082436213,
      "disagreement_subset": {
        "nll": 0.8085730386845184,
        "accuracy": 0.6656716417910448,
        "brier": 0.4951459082436213
      }
    },
    {
      "model": "B0",
      "k": 4,
      "nll": 0.8085730386845184,
      "accuracy": 0.6656716417910448,
      "brier": 0.4951459082436213,
      "disagreement_subset": {
        "nll": 0.8085730386845184,
        "accuracy": 0.6656716417910448,
        "brier": 0.4951459082436213
      }
    },
    {
      "model": "B0",
      "k": 16,
      "nll": 0.8085730386845184,
      "accuracy": 0.6656716417910448,
      "brier": 0.4951459082436213,
      "disagreement_subset": {
        "nll": 0.8085730386845184,
        "accuracy": 0.6656716417910448,
        "brier": 0.4951459082436213
      }
    },
    {
      "model": "B0",
      "k": 64,
      "nll": 0.8085730386845184,
      "accuracy": 0.6656716417910448,
      "brier": 0.4951459082436213,
      "disagreement_subset": {
        "nll": 0.8085730386845184,
        "accuracy": 0.6656716417910448,
        "brier": 0.4951459082436213
      }
    },
    {
      "model": "B1",
      "k": 0,
      "nll": 0.8085730386845184,
      "accuracy": 0.6656716417910448,
      "brier": 0.4951459082436213,
      "disagreement_subset": {
        "nll": 0.8085730386845184,
        "accuracy": 0.6656716417910448,
        "brier": 0.4951459082436213
      }
    },
    {
      "model": "B1",
      "k": 4,
      "nll": 0.7759772896254553,
      "accuracy": 0.6398009950248756,
      "brier": 0.477265009265505,
      "disagreement_subset": {
        "nll": 0.7759772896254553,
        "accuracy": 0.6398009950248756,
        "brier": 0.477265009265505
      }
    },
    {
      "model": "B1",
      "k": 16,
      "nll": 0.7086084725935544,
      "accuracy": 0.6549751243781095,
      "brier": 0.4347953774067855,
      "disagreement_subset": {
        "nll": 0.7086084725935545,
        "accuracy": 0.6549751243781095,
        "brier": 0.4347953774067855
      }
    },
    {
      "model": "B1",
      "k": 64,
      "nll": 0.6696272984755983,
      "accuracy": 0.6641791044776119,
      "brier": 0.418761371612179,
      "disagreement_subset": {
        "nll": 0.6696272984755983,
        "accuracy": 0.6641791044776119,
        "brier": 0.418761371612179
      }
    },
    {
      "model": "B2",
      "k": 0,
      "nll": 0.7930565015105159,
      "accuracy": 0.6619402985074627,
      "brier": 0.4815180581616308,
      "disagreement_subset": {
        "nll": 0.7930565015105159,
        "accuracy": 0.6619402985074627,
        "brier": 0.4815180581616308
      }
    },
    {
      "model": "B2",
      "k": 4,
      "nll": 0.7930565015105159,
      "accuracy": 0.6619402985074627,
      "brier": 0.4815180581616308,
      "disagreement_subset": {
        "nll": 0.7930565015105159,
        "accuracy": 0.6619402985074627,
        "brier": 0.4815180581616308
      }
    },
    {
      "model": "B2",
      "k": 16,
      "nll": 0.7930565015105159,
      "accuracy": 0.6619402985074627,
      "brier": 0.4815180581616308,
      "disagreement_subset": {
        "nll": 0.7930565015105159,
        "accuracy": 0.6619402985074627,
        "brier": 0.4815180581616308
      }
    },
    {
      "model": "B2",
      "k": 64,
      "nll": 0.7930565015105159,
      "accuracy": 0.6619402985074627,
      "brier": 0.4815180581616308,
      "disagreement_subset": {
        "nll": 0.7930565015105159,
        "accuracy": 0.6619402985074627,
        "brier": 0.4815180581616308
      }
    },
    {
      "model": "B3",
      "k": 0,
      "nll": 0.7930565015105159,
      "accuracy": 0.6619402985074627,
      "brier": 0.4815180581616308,
      "disagreement_subset": {
        "nll": 0.7930565015105159,
        "accuracy": 0.6619402985074627,
        "brier": 0.4815180581616308
      }
    },
    {
      "model": "B3",
      "k": 4,
      "nll": 0.79145073633967,
      "accuracy": 0.6298507462686567,
      "brier": 0.48418389423904507,
      "disagreement_subset": {
        "nll": 0.79145073633967,
        "accuracy": 0.6298507462686567,
        "brier": 0.48418389423904507
      }
    },
    {
      "model": "B3",
      "k": 16,
      "nll": 0.698957109269533,
      "accuracy": 0.6708955223880597,
      "brier": 0.4235431242072849,
      "disagreement_subset": {
        "nll": 0.698957109269533,
        "accuracy": 0.6708955223880597,
        "brier": 0.4235431242072849
      }
    },
    {
      "model": "B3",
      "k": 64,
      "nll": 0.6768720778908367,
      "accuracy": 0.6753731343283582,
      "brier": 0.4102007866489577,
      "disagreement_subset": {
        "nll": 0.6768720778908367,
        "accuracy": 0.6753731343283582,
        "brier": 0.4102007866489577
      }
    },
    {
      "model": "B4",
      "k": 0,
      "nll": 0.7930565015105159,
      "accuracy": 0.6619402985074627,
      "brier": 0.4815180581616308,
      "disagreement_subset": {
        "nll": 0.7930565015105159,
        "accuracy": 0.6619402985074627,
        "brier": 0.4815180581616308
      }
    },
    {
      "model": "B4",
      "k": 4,
      "nll": 0.7588221140242096,
      "accuracy": 0.6659203980099503,
      "brier": 0.46058621801300664,
      "disagreement_subset": {
        "nll": 0.7588221140242096,
        "accuracy": 0.6659203980099503,
        "brier": 0.46058621801300664
      }
    },
    {
      "model": "B4",
      "k": 16,
      "nll": 0.709913380921825,
      "accuracy": 0.6721393034825871,
      "brier": 0.42832731496570875,
      "disagreement_subset": {
        "nll": 0.7099133809218251,
        "accuracy": 0.6721393034825871,
        "brier": 0.42832731496570875
      }
    },
    {
      "model": "B4",
      "k": 64,
      "nll": 0.6947476964497054,
      "accuracy": 0.6723880597014925,
      "brier": 0.41996740506961244,
      "disagreement_subset": {
        "nll": 0.6947476964497051,
        "accuracy": 0.6723880597014925,
        "brier": 0.41996740506961244
      }
    },
    {
      "model": "M1",
      "k": 0,
      "nll": 0.7930565015105159,
      "accuracy": 0.6619402985074627,
      "brier": 0.4815180581616308,
      "disagreement_subset": {
        "nll": 0.7930565015105159,
        "accuracy": 0.6619402985074627,
        "brier": 0.4815180581616308
      }
    },
    {
      "model": "M1",
      "k": 4,
      "nll": 0.7914507363331946,
      "accuracy": 0.6298507462686567,
      "brier": 0.48418389423551367,
      "disagreement_subset": {
        "nll": 0.7914507363331946,
        "accuracy": 0.6298507462686567,
        "brier": 0.48418389423551367
      }
    },
    {
      "model": "M1",
      "k": 16,
      "nll": 0.6989571092685489,
      "accuracy": 0.6708955223880597,
      "brier": 0.42354312420644513,
      "disagreement_subset": {
        "nll": 0.698957109268549,
        "accuracy": 0.6708955223880597,
        "brier": 0.42354312420644513
      }
    },
    {
      "model": "M1",
      "k": 64,
      "nll": 0.6768720778896995,
      "accuracy": 0.6753731343283582,
      "brier": 0.41020078664806275,
      "disagreement_subset": {
        "nll": 0.6768720778896995,
        "accuracy": 0.6753731343283582,
        "brier": 0.41020078664806275
      }
    }
  ],
  "seed_diagnostics": [
    {
      "seed": 11,
      "nll": 0.6989571092666284
    },
    {
      "seed": 29,
      "nll": 0.6989571092694021
    },
    {
      "seed": 47,
      "nll": 0.6989571092696165
    }
  ],
  "history_controls": [
    {
      "model": "B3",
      "true_nll": 0.698957109269533,
      "shuffled_nll": 0.8753662237713945,
      "true_history_advantage": 0.17640911450186136
    },
    {
      "model": "B4",
      "true_nll": 0.7099133809218251,
      "shuffled_nll": 0.83057855635581,
      "true_history_advantage": 0.1206651754339848
    },
    {
      "model": "M1",
      "true_nll": 0.6989571092685491,
      "shuffled_nll": 0.8753662237708948,
      "true_history_advantage": 0.17640911450234567
    }
  ],
  "adaptation_person_solves": 3300,
  "artifacts": [
    {
      "filename": "development_predictions.npz",
      "bytes": 3130407,
      "sha256": "e3cad4f0db5556d9f659daf2b79dbe6f806918b60266983e7bc9bb9c3427097b"
    },
    {
      "filename": "development_paired_losses.npz",
      "bytes": 113931,
      "sha256": "7bd72bd4aa5d24a402f9e9c2dded892e590a6bc8b7bcb1c7988472cc1847e272"
    }
  ]
}
```
