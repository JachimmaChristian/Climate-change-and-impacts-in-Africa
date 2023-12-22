
def solution_1_tests():
    # THE CHECK FUNCTIONS

    def df_cols_to_sorted_list(df):
        return df.columns.str.lower().sort_values().tolist()

    # ' The function checks if the dataset columns were renamed
    # ' according to the instructions
    def columns_were_renamed(ipcc_2006_africa, totals_by_country_africa):

        d1 = 'ipcc_2006_africa'
        d2 = 'totals_by_country_africa'

        def rename_msg(old, new, dataset_name):
            return f'Have you renamed {old} column to {new} in the {dataset_name} dataset?\n'

        # Arrange
        ipcc_cols = df_cols_to_sorted_list(ipcc_2006_africa)
        totals_cols = df_cols_to_sorted_list(totals_by_country_africa)

        # Check if the columns have been renamed
        assert (
            'c_group_im24_sh' not in ipcc_cols) and (
            'region' in ipcc_cols), rename_msg(
            'C_group_IM24_sh', 'Region', d1)

        assert (
            'country_code_a3' not in ipcc_cols) and (
            'code' in ipcc_cols), rename_msg(
            'Country_code_A3', 'Code', d1)

        assert (
            'ipcc_code_2006_for_standard_report_name' not in ipcc_cols) and (
            'industry' in ipcc_cols), rename_msg(
            'ipcc_code_2006_for_standard_report_name', 'Industry', d1)

        assert (
            'c_group_im24_sh' not in totals_cols) and (
            'region' in totals_cols), rename_msg(
            'C_group_IM24_sh', 'Region', d2)

        assert (
            'country_code_a3' not in totals_cols) and (
            'code' in totals_cols), rename_msg(
            'Country_code_A3', 'Code', d2)

    # ' The function checks if columns IPCC_annex, ipcc_code_2006_for_standard_report, and Substance were dropped

    def columns_were_dropped(ipcc_2006_africa, totals_by_country_africa):

        # Arrange
        ipcc_cols = df_cols_to_sorted_list(ipcc_2006_africa)
        totals_cols = df_cols_to_sorted_list(totals_by_country_africa)

        d1 = 'ipcc_2006_africa'
        d2 = 'totals_by_country_africa'

        def drop_msg(col, dataset_name):
            return f'Did you drop {col} column from {dataset_name} dataset? Please check your code!\n'

        assert 'ipcc_annex' not in ipcc_cols, drop_msg('IPCC_annex', d1)

        assert 'ipcc_code_2006_for_standard_report' not in ipcc_cols, drop_msg(
            'ipcc_code_2006_for_standard_report', d1)

        assert 'substance' not in ipcc_cols, drop_msg('Substance', d1)

        assert 'ipcc_annex' not in totals_cols, drop_msg('IPCC_annex', d2)

        assert 'substance' not in totals_cols, drop_msg('Substance', d2)

    def column_years_was_gathered(
            ipcc_2006_africa, totals_by_country_africa):

        ipcc_cols = df_cols_to_sorted_list(ipcc_2006_africa)
        totals_cols = df_cols_to_sorted_list(totals_by_country_africa)

        # Check if the number of columns match the expected number
        assert len(
            ipcc_cols) == 7, "Have you used converted the ipcc_2006_africa dataset from wide to long format?"

        assert len(
            totals_cols) == 5, "Have you converted the totals_by_country_africa dataset from wide to long format?"

        # Check if the year columns have been gathered into Year and CO2
        assert ipcc_cols == ['co2', 'code', 'fossil_bio', 'industry', 'name', 'region',
                             'year'], "Have you gathered the ipcc_2006_africa year columns into Year and CO2?"

        assert totals_cols == ['co2', 'code', 'name', 'region',
                               'year'], "Have you gathered the totals_by_country_africa year columns into Year and CO2?"

    def co2_col_has_no_nas(ipcc_2006_africa, totals_by_country_africa):

        # Check that rows with missing CO2 have been dropped
        assert ipcc_2006_africa[ipcc_2006_africa.CO2.isnull(
        )].size == 0, 'Did you drop the rows with missing CO2 in the ipcc_2006_africa dataset?'

        assert totals_by_country_africa[totals_by_country_africa.CO2.isnull(
        )].size == 0, 'Did you drop the rows with missing CO2 in the totals_by_country_africa dataset?'

    def year_col_has_int_type(ipcc_2006_africa, totals_by_country_africa):
        # Check that Year column is an integer
        assert ipcc_2006_africa.Year.dtype == int, "Have you converted the ipcc_2006_africa's Year column to an integer?"

        assert totals_by_country_africa.Year.dtype == int, "Have you converted the totals_by_country_africa's Year column to an integer?"

    def run_all(ipcc_2006_africa, totals_by_country_africa):
        columns_were_renamed(ipcc_2006_africa, totals_by_country_africa)
        columns_were_dropped(ipcc_2006_africa, totals_by_country_africa)
        column_years_was_gathered(
            ipcc_2006_africa, totals_by_country_africa)
        co2_col_has_no_nas(ipcc_2006_africa, totals_by_country_africa)
        year_col_has_int_type(ipcc_2006_africa, totals_by_country_africa)

    return run_all


def check_task_1(ipcc_2006_africa, totals_by_country_africa):
    run_all = solution_1_tests()
    run_all(ipcc_2006_africa, totals_by_country_africa)


def check_task_3(relationship_btw_time_CO2):

    # Helper

    def get_coeff(Region):
        coeff = relationship_btw_time_CO2.loc[(Region, 'Year'), 'CO2']
        return round(coeff, 3)

    # Check if the correlation table matches an expected dimension
    assert relationship_btw_time_CO2.shape == (
        8, 2), "Have you created relationship_btw_time_CO2 variable?"

    coeffs = (
        get_coeff('Eastern_Africa'),
        get_coeff('Northern_Africa'),
        get_coeff('Southern_Africa'),
        get_coeff('Western_Africa'))

    expected = (0.182, 0.43, 0.261, 0.324)

    assert coeffs == expected, f"Expected {expected} but got {coeffs}. Did you use Spearman's correlation? Please, check your code!"


def check_task_4(aov_results, pw_ttest_result):
    assert aov_results.shape == (
        1, 6), "Have you conducted an ANOVA using pingouin.anova()?"
    p_value = round(aov_results.loc[0, 'p-unc'], 3)
    f_value = round(aov_results.loc[0, 'F'], 3)

    assert f_value == 35.558, "The F value of your ANOVA doesn't seem to be correct. Please, check your code!"
    assert p_value == 0, "The p-value of your ANOVA doesn't seem to be correct. Please, check your code!"

    assert pw_ttest_result.shape == (
        6, 13), "Have you conducted a pairwise t-test using pingouin.pairwise_tests()?"

    selected = pw_ttest_result.query(
        "A == 'Northern_Africa' and B == 'Southern_Africa'").reset_index()

    assert selected.loc[0, 'p-corr'] == 1, "Seems like your pingouin.pairwise_tests() call isn't correct! Please, check your code!"


def check_task_5(top_5_industries):
    # Check if the DataFrame has the correct columns
    expected_cols = ['Region', 'Industry', 'Count']
    cols = list(top_5_industries.columns)

    assert cols == expected_cols, f"Incorrect columns in 'top_5_industries' DataFrame. Expected {expected_cols} but got {cols}"

    # Check if the DataFrame has the correct shape (rows, columns)
    assert top_5_industries.shape == (
        20, 3), "Seems like not all the Regions are included. Please, check your code!"

    # Check if each region contains exactly 5 industries
    assert top_5_industries['Region'].value_counts().min(
    ) == 5, "Not all regions have exactly 5 industries."

    # Check if the industries are sorted within each region by count in
    # descending order
    for region, region_df in top_5_industries.groupby('Region'):
        counts_sorted_desc = region_df['Count'].tolist(
        ) == sorted(region_df['Count'], reverse=True)
        assert counts_sorted_desc, f"Industries are not sorted by count in descending order for Region: {region}"

    # Check if the count values are positive integers
    assert top_5_industries['Count'].dtype == 'int64', "Count values should be of integer type."

    # Check if the count values sum is correct
    assert top_5_industries['Count'].sum(
    ) == 20907, "Count values returned are not correct."


def check_task_6(max_co2_industries):
    # Define the expected result
    expected_result = {
        'Eastern_Africa': ('Residential and other sectors', 7904.44),
        'Northern_Africa': ('Main Activity Electricity and Heat Production', 13612.23),
        'Southern_Africa': ('Main Activity Electricity and Heat Production', 11377.80),
        'Western_Africa': ('Residential and other sectors', 8702.94)
    }

    # Check if the DataFrame has the correct columns
    assert list(max_co2_industries.columns) == [
        'Region', 'Industry', 'CO2'], "The columns in 'max_co2_industries' DataFrame are incorrect."

    # Check if the DataFrame has the correct shape (rows, columns)
    assert max_co2_industries.shape[0] == len(
        expected_result), "The number of rows in 'max_co2_industries' does not match the expected result."

    # Check if the CO2 values are non-negative floats
    assert max_co2_industries['CO2'].dtype == float, "CO2 values should be of floating-point type."
    assert (max_co2_industries['CO2'] >= 0).all(
    ), "Some CO2 values are negative."

    # Check if the data for each region matches the expected result
    for _, row in max_co2_industries.iterrows():
        region = row['Region']
        industry = row['Industry']
        co2_value = round(row['CO2'], 2)
        expected_industry, expected_co2_value = expected_result[region]

        assert industry == expected_industry, f"The industry for Region '{region}' is incorrect."
        assert co2_value == expected_co2_value, f"The CO2 value for Region '{region}' is incorrect. Expected {expected_co2_value} but got {co2_value}."


def check_task_7(predicted_co2):
    expected_vals = [15177.72, 10788.07, 37761.69, 41081.90]
    predicted_co2.sort()
    expected_vals.sort()

    assert list(
        predicted_co2) == expected_vals, f"The expected values for are {expected_vals} respectively! Did you convert from log10 to decimals?"


def check_task_8(joined, model_temp):
    expected = (208, 4)
    current = joined.shape

    assert current == expected, f"Excepted the dimension of joined to be {expected} but {current} was provided. Please, check your code!"

    val = round(model_temp.rsquared_adj, 2)

    assert val == 0.98, f"Expected an adjusted r.squared of 0.98 but got {val}. Please, check your model"

    co2_est = model_temp.params[4]

    assert round(
        co2_est, 2) == 1.95, "The coefficient of log10(CO2) is not 1.95. Please, check your code!"
