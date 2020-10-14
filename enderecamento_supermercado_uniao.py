  # ['4990 ~ 4999 - Número de série', 4990, 'STR16', 'ENUM'],
  # ['5001 - Potência ativa nominal', 5001, 'U16', 'FIX1'], # 0,1kWh
  # ['5003 - Rendimentos de potência diários', 5003, 'U16', 'FIX1'], # 0,1kWh
  # ['5004 - Rendimento total de energia', 5004, 'U32', 'FIX0'], #kWh
  # ['5006 - Tempo total de execução', 5006, 'U32', 'Duração'], # horas
  # ['5008 - Temperatura interna', 5008, 'S16', 'FIX1'], #C
  # ['5009 - Potência aparente total', 5009, 'U32', 'FIX0'], #VA
  [ '5011 - MPPT 1 tensão' , 5011 , 'U16' , 'FIX1' ], # 0.1V
  # ['5012 - MPPT 1 atual', 5012, 'U16', 'FIX1'], # 0.1A
  [ '5013 - MPPT 2 voltagem' , 5013 , 'U16' , 'FIX1' ], # 0,1V
  # ['5014 - MPPT 2 atual', 5014, 'U16', 'FIX1'], # 0.1A
  # ['5015 - MPPT 3 tensão', 5015, 'U16', 'FIX1'], # 0,1V
  # ['5016 - MPPT 3 atual', 5016, 'U16', 'FIX1'], # 0.1A
  # ['5017 - Potência DC total', 5017, 'U32', 'FIX0'], #Watts
  # ['5019 - Tensão da Fase A', 5019, 'U16', 'FIX1'], # 0.1V
  # ['5020 - Tensão da fase B', 5020, 'U16', 'FIX1'], # 0,1V
  # ['5021 - Tensão da Fase C', 5021, 'U16', 'FIX1'], # 0.1V
  # ['5022 - Corrente da fase A', 5022, 'U16', 'FIX1'], # 0.1A
  # ['5023 - Corrente da fase B', 5023, 'U16', 'FIX1'], # 0.1A
  # ['5024 - Corrente da fase C', 5024, 'U16', 'FIX1'], # 0.1A
  [ '5031 - Potência ativa total' , 5031 , 'U32' , 'FIX0' ], #Watts
  # ['5033 - Potência reativa total', 5033, 'S32', 'FIX0'], #variância
  # ['5035 - Fator de potência', 5035, 'S16', 'FIX1000'], # 0,001
  # ['5036 - Frequência de grade', 5036, 'U16', 'FIX1'], # 0,1 Hz
  # ['5049 - Potência reativa nominal', 5049, 'U16', 'FIX1'], #kilovariance
  # ['5083 - Potência do medidor', 5083, 'S32', 'FIX'], #W
  # ['5085 - Potência da fase do medidor A', 5085, 'S32', 'FIX'], #W
  # ['5087 - Potência da fase do medidor B', 5087, 'S32', 'FIX'], #W
  # ['5089 - Potência da fase C do medidor', 5089, 'S32', 'FIX'], #W
  # ['5097 - Importação de energia diária', 5097, 'U32', 'FIX1'], # 0,1 kWh
  # ['5113 - Tempo de execução diário', 5113, 'U16', 'Duração'], # minutos
  # ['5144 - Rendimentos totais de potência', 5144, 'U32', 'FIX1'], # 0,1 kWh
  # ['5146 - Tensão negativa para aterramento', 5146, 'S16', 'FIX1'], # 0,1V
  [ '5148 - Frequência da rede' , 5148 , 'U16' , 'FIX2' ] # 0,01 Hz
  
  
  "5001":  "5001",
  "5003":  "5003",
  "5004":  "5004",
  "5005":  "5005",
  "5006":  "5006",        
  "5007":  "5007",    
  "5008":  "internal_temp_10",
  "5009":  "5009",    
  "5011":  "pv1_voltage_10",
  "5012":  "pv1_current_10",
  "5013":  "pv2_voltage_10",
  "5014":  "pv2_current_10",
  "5015":  "5015",    
  "5016":  "5016",    
  "5017":  "total_pv_power",
  "5018":  "5018",    
  "5019":  "grid_voltage_10",
  "5020":  "5020",    
  "5021":  "5021",    
  "5022":  "inverter_current_10",
  "5023":  "5023",    
  "5031":  "5031",
  "5032":  "5032",
  "5036":  "grid_frequency_10",
  "5037":  "5037",
  "13001": "running_state",
  "13002": "daily_pv_energy_10",
  "13003": "total_pv_energy_10",
  "13004": "13004",
  "13005": "daily_export_energy_10",
  "13006": "total_export_energy_10",
  "13007": "13007",
  "13008": "load_power",
  "13009": "13009",
  "13010": "export_power",
  "13011": "grid_import_or_export",
  "13012": "daily_charge_energy_10",
  "13013": "total_charge_energy_10",
  "13014": "13014",
  "13015": "co2_emission_reduction",
  "13016": "13016",
  "13017": "daily_use_energy_10",
  "13018": "total_use_energy_10",
  "13019": "13019",
  "13020": "battery_voltage_10",
  "13021": "battery current_10",
  "13022": "battery_power",
  "13023": "battery_level_10",
  "13024": "battery_health_10",
  "13025": "battery_temp_10",
  "13026": "daily_discharge_energy_10",
  "13027": "total_discharge_energy_10",
  "13028": "13028",
  "13029": "use_power",
  "13030": "13030",
  "13031": "inverter_current_10",
  "13032": "13032",
  "13033": "13033",
  "13034": "pv_power",
  "13035": "13035",
  "13036": "13036",
  "13037": "13037",
  "13038": "13038"
