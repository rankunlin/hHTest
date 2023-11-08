import cabinetry
cabinetry.set_logging()

cabinetry_config = cabinetry.configuration.load('hHTest.yaml')
cabinetry.configuration.print_overview(cabinetry_config)

cabinetry.templates.build(cabinetry_config, method="uproot")
cabinetry.templates.postprocess(cabinetry_config)

workspace_path = "workspace/hHTest.json"
ws = cabinetry.workspace.build(cabinetry_config)
cabinetry.workspace.save(ws, workspace_path)

model, data = cabinetry.model_utils.model_and_data(ws)
cabinetry.visualize.modifier_grid(model)

fit_results = cabinetry.fit.fit(model, data)

model_pred = cabinetry.model_utils.prediction(model)
figures = cabinetry.visualize.data_mc(model_pred, data, config=cabinetry_config)

model_pred_postfit = cabinetry.model_utils.prediction(model, fit_results=fit_results)
_ = cabinetry.visualize.data_mc(model_pred_postfit, data, config=cabinetry_config)

limit_results = cabinetry.fit.limit(model, data)
cabinetry.visualize.limit(limit_results)
