# We're wrapping each solution in functions solely for the sake of organization

def solution_one(ipcc_2006_africa, totals_by_country_africa):
    # Instruction 1 Solution wrapped in a function
    # rename columns
    ipcc_2006_africa = ipcc_2006_africa.rename(columns={'C_group_IM24_sh': 'Region', 'Country_code_A3': 'Code',
                                                        'ipcc_code_2006_for_standard_report_name': 'Industry'})

    totals_by_country_africa = totals_by_country_africa.rename(
        columns={
            'C_group_IM24_sh': 'Region',
            'Country_code_A3': 'Code'})

    # drop columns
    ipcc_2006_africa = ipcc_2006_africa.drop(['IPCC_annex',
                                              'ipcc_code_2006_for_standard_report',
                                              'Substance'],
                                             axis=1)

    totals_by_country_africa = totals_by_country_africa.drop(
        ['IPCC_annex', 'Substance'], axis=1)

    # Melt and clean Year column

    def melt_clean(df):
        value_vars = list(filter(lambda x: x.startswith('Y_'), df.columns))
        id_vars = list(set(df.columns).difference(value_vars))

        # melt
        long = df.melt(
            id_vars=id_vars,
            value_vars=value_vars,
            var_name='Year',
            value_name='CO2')

        # drop rows where co2 is missing
        long = long[~long.CO2.isnull()]

        # convert year to integer
        long.Year = long.Year.str.replace('Y_', '').astype(int)

        return long

    ipcc_2006_africa = melt_clean(ipcc_2006_africa)
    totals_by_country_africa = melt_clean(totals_by_country_africa)
    # Solution ends here

    return ipcc_2006_africa, totals_by_country_africa


def solution_two(g):
    # Retrieve sns and plt from the global namespace
    # Since we wrapped this code in a function.
    sns = g['sns']
    plt = g['plt']
    totals_by_country_africa = g['totals_by_country_africa']

    # Only this part is required for your notebook
    sns.lineplot(
        x='Year',
        y='CO2',
        hue='Region',
        data=totals_by_country_africa,
        ci=None)
    plt.title('CO2 levels across the African Regions between 1970 and 2021')
    plt.ylabel('CO2 (kt)')
    # Solution ends here


def solution_three(g):
    # Retrieve totals_by_country_africa from the global namespace
    # Since we wrapped this code in a function.
    totals_by_country_africa = g['totals_by_country_africa']

    # The actual solution for your notebook
    relationship_btw_time_CO2 = totals_by_country_africa.groupby(
        'Region')[['Year', 'CO2']].corr(method='spearman')
    # Solution ends here

    # Return for testing purposes
    return relationship_btw_time_CO2


def solution_four(g):
    # Retrieve totals_by_country_africa and pingouin from the global namespace
    # Since we wrapped this code in a function.
    pingouin = g['pingouin']
    totals_by_country_africa = g['totals_by_country_africa']

    # The actual solution for your notebook
    aov_results = pingouin.anova(
        data=totals_by_country_africa,
        dv='CO2',
        between='Region')
    pw_ttest_result = pingouin.pairwise_tests(
        data=totals_by_country_africa,
        dv='CO2',
        between='Region',
        padjust="bonf").round(3)
    # Solution ends here

    # Return for testing purposes
    return aov_results, pw_ttest_result


def solution_five(ipcc_2006_africa):

    # Group the data by Region and Industry and count the occurrences
    grouped = ipcc_2006_africa.groupby(
        ['Region', 'Industry']).size().reset_index(name='Count')

    # Sort the data within each region group by Count in descending order
    grouped = grouped.sort_values(['Region', 'Count'], ascending=[True, False])

    # Get the top 5 industries for each region
    top_5_industries = grouped.groupby('Region').head(5).reset_index(drop=True)

    return top_5_industries


def solution_six(ipcc_2006_africa):
    # Group the data by Region and Industry, and calculate the average CO2
    # emissions for each group
    grouped = ipcc_2006_africa.groupby(['Region', 'Industry'])[
        'CO2'].mean().reset_index()

    # Find the industry with the maximum average CO2 emissions in each region
    max_co2_industries = grouped.loc[grouped.groupby(
        'Region')['CO2'].idxmax()].reset_index(drop=True)

    # Return the result
    return max_co2_industries


def solution_seven(reg, totals_by_country_africa, newdata, g):
    # Retrieve pandas pd and numpy np from the global namespace
    # Since we wrapped this code in a function.
    pd = g['pd']
    np = g['np']

    # The actual solution for your notebook
    target = np.log10(totals_by_country_africa['CO2'])
    feats = pd.get_dummies(totals_by_country_africa[['Year', 'Region']])
    reg.fit(feats, target)
    predicted_co2 = reg.predict(newdata)
    predicted_co2 = np.round(10**predicted_co2, 2)
    # Solution ends here

    # Return the predicted_co2 for testing purposes
    return predicted_co2


def solution_eight(totals_by_country_africa, temperatures, g):
    # Take pandas pd from global namespace
    pd = g['pd']
    OLS = g['OLS']
    np = g['np']  # do not remove

    # The actual solution for your notebook
    countries = ["Ethiopia", "Mozambique", "Nigeria", "Tunisia"]
    selected_countries = totals_by_country_africa[[
        'Name', 'Year', 'CO2']].query('Name in @countries')
    temp_long = temperatures.melt(
        id_vars=['Year'],
        value_vars=countries,
        var_name='Name',
        value_name='Temperature')

    joined = pd.merge(
        selected_countries, temp_long, on=[
            'Name', 'Year'], how='inner')

    model_temp = OLS.from_formula(
        "Temperature ~ np.log10(CO2) + Name",
        data=joined).fit()
    # Solution ends here

    # For testing purposes
    return joined, model_temp
