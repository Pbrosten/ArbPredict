import numpy as np

def scaler(x): 
    avg = x.mean()
    std = x.std()
    return (x-avg)/std

def df_scaler(df, cols):
    df0 = df.copy()
    for c in cols:
        df0[f"{c}_sc"] = scaler(df0[c])
        df0 = df0.drop(c,axis=1)
    return df0

def fourthYear(playedYears):
    if len(playedYears) >= 4:
        return playedYears[3]
    else:
        return 0

def rookieMean(careerStats):
    return careerStats[:3].mean()

def rookieSum(careerStats):
    return sum(careerStats[:3])

def rookiePos(df_pos):
    df_pos_rookie =  df_pos[df_pos['yearID'] <= df_pos['yearID'].array[0]+2]
    pos_grp = df_pos_rookie.groupby(['POS'])['InnOuts'].unique()
    pos_totals = np.array([])
    for pos in pos_grp:
        pos_totals = np.append(pos_totals,pos.sum())
    return pos_grp.reset_index()['POS'].array[pos_totals.argmax()]