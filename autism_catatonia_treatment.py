import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Streamlit Page Title
st.title("Medication Treatment Analysis Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload your data file", type=["csv", "xlsx"])

if uploaded_file:
    # Load the data depending on file type
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)

    st.subheader("1. Most Common Side Effects")
    side_effect_counts = df['Side_Effects'].value_counts()
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    side_effect_counts.plot(kind='bar', color='skyblue', ax=ax1)
    ax1.set_title('Most Common Side Effects')
    ax1.set_xlabel('Side Effect')
    ax1.set_ylabel('Count')
    ax1.tick_params(axis='x', rotation=45)
    st.pyplot(fig1)

    st.subheader("2. Improvement by Presence of Side Effects")
    df['Has_Side_Effects'] = df['Side_Effects'].notna() & (df['Side_Effects'].str.strip() != '')
    df['Side Effects Present'] = df['Has_Side_Effects'].map({True: 'Yes', False: 'No'})
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=df, x='Side Effects Present', y='Improvement (%)',
                hue='Side Effects Present', palette='pastel', ax=ax2)
    ax2.set_title('Improvement (%) by Side Effects Presence')
    st.pyplot(fig2)

    st.subheader("3. Improvement by Gender")
    fig3, ax3 = plt.subplots(figsize=(8, 6))
    sns.boxplot(x='Gender', y='Improvement (%)', data=df, ax=ax3)
    ax3.set_title('Improvement (%) by Gender')
    st.pyplot(fig3)

    st.subheader("4. Age vs. Improvement (%)")
    fig4 = sns.lmplot(x='Age', y='Improvement (%)', data=df, height=6, aspect=1.5)
    fig4.set(title='Age vs Improvement (%)')
    st.pyplot(fig4.figure)  # Use .figure to render lmplot

    fig5, ax5 = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='Age', y='Improvement (%)', data=df, ax=ax5)
    ax5.set_title('Age vs Improvement (%)')
    st.pyplot(fig5)

    st.subheader("5. Treatment Duration vs. Improvement")
    treated_df = df[df['Duration_Days'] > 0]
    fig6, ax6 = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=treated_df, x='Duration_Days', y='Improvement (%)', hue='Medication', palette='Set2', s=100, ax=ax6)
    sns.regplot(data=treated_df, x='Duration_Days', y='Improvement (%)', scatter=False, color='black', line_kws={"linestyle":"--"}, ax=ax6)
    ax6.set_title('Duration of Treatment vs. Improvement (%)')
    st.pyplot(fig6)

    st.subheader("6. Top 5 Responders by Medication")
    df_top = df.groupby('Medication').apply(
        lambda group: group.sort_values('Improvement (%)', ascending=False).head(5)
    ).reset_index(drop=True)

    df_melted = df_top.melt(
        id_vars=['ID', 'Medication'],
        value_vars=['Pre_Treatment_Score', 'Post_Treatment_Score'],
        var_name='Treatment_Stage',
        value_name='Score'
    )

    g = sns.catplot(
        data=df_melted,
        x='ID', y='Score', hue='Treatment_Stage',
        col='Medication', kind='bar',
        col_wrap=3, height=4, aspect=1.5,
        palette='muted'
    )
    g.set_titles("Medication: {col_name}")
    g.set_xticklabels(rotation=45)
    st.pyplot(g.figure)

    st.subheader("7. Interactive Bar Chart: Pre vs Post Treatment Scores")
    df_melted2 = df.melt(
        id_vars='ID',
        value_vars=['Pre_Treatment_Score', 'Post_Treatment_Score'],
        var_name='Stage',
        value_name='Score'
    )

    fig = px.bar(
        df_melted2, x='ID', y='Score', color='Stage',
        title='Pre vs Post Treatment Scores',
        barmode='group'
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)
