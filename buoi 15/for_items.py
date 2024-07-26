import pandas as pd

df = pd.DataFrame({'species': ['bear', 'bear', 'marsupial'],
                  'population': [1864, 22000, 80000]},
                  index=['panda', 'polar', 'koala'])

for label, content in df.items():
    print(f"label: {label}")
    print(f'content: {content}', sep = "\n")