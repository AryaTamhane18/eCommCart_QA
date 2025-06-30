from behave.__main__ import main

if __name__ == "__main__":
    main([
        '--tags=@login,@sorting,@AddToCart,@RemoveItem,@CartValidation,@GeoAPI',
        '--format=allure_behave.formatter:AllureFormatter',
        '--outfile=Temp_reports/allure_reports',
        'Features/Feature_files'
    ])
