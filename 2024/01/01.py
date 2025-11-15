import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    f = open("./input.txt")
    i = 0
    for line in f:
        i+=1
        if i == 500:
            print(line)
            print(type(line))
            cacca = line.split(sep="   ")
            print(cacca[1][:-1])
    print(i)
    return


@app.cell
def _(pd):
    df = pd.read_table("./input.txt", sep= "   ", header=None)
    df
    return (df,)


@app.cell
def _(df):
    A = df[0].sort_values()
    B = df[1].sort_values()
    #distances = []
    total_distance = 0
    '''
    for j in range(len(df[0])):
        #print("Eseguo: ", A[j], " - ", B[j])
        diff = abs(df[0].sort_values()[j] - df[1].sort_values()[j])
        total_distance += diff
        #distances.append(diff)
    print("distanza totale:", total_distance)
    #print(distances)
    '''
    for a, b in zip(A, B):
        total_distance += abs(a - b)
    print(total_distance)
    return A, B


@app.cell
def _(A, B):
    #print(A.value_counts().to_dict())
    B_freq = B.value_counts().to_dict()
    total_similarity = 0
    for elemento_a in A:
        similarity = elemento_a * B_freq.get(elemento_a, 0)
        #print(similarity)
        total_similarity += similarity

    print('total similarity: ', total_similarity)
    return (B_freq,)


@app.cell
def _(B_freq):
    B_freq[69869]
    return


@app.cell
def _(B):
    len(B)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
