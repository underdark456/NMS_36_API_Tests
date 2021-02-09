inroute_acm = ['inacm_enable','tdmrf_acm_offset']

modulator = ['modulator_txon', 'modulator_txlvl']

tdm_tx = ['tdmtx_freq', 'tdmtx_symrate', 'tdmtx_fec', 'modulator_rolloff', 'modulator_pilots']

acm = ['acm_enable', 'acm_fec2', 'acm_fec3', 'acm_fec4', 'acm_fec5', 'acm_fec6', 'acm_fec7', 'acm_fec8',
       'acm_cnremote']
tdm_rx = ['tdmrx_input', 'tdmrx_freq', 'tdmrx_symrate']

tdma_rf = ['tdmrf_input', 'tdmrf_symrate', 'tdmrf_fec', 'tdmrf_rolloff_5', 'ldpc',
           'tdmrf_txfreq_0','tdmrf_rxfreq_0',
           'tdmrf_txfreq_1','tdmrf_rxfreq_1',
           'tdmrf_txfreq_2','tdmrf_rxfreq_2',
           'tdmrf_txfreq_3','tdmrf_rxfreq_3',
           'tdmrf_txfreq_4','tdmrf_rxfreq_4',
           'tdmrf_txfreq_5','tdmrf_rxfreq_6',
           'tdmrf_txfreq_6','tdmrf_rxfreq_7',
           'tdmrf_txfreq_7','tdmrf_rxfreq_8',
           'tdmrf_txfreq_8','tdmrf_rxfreq_9',
           'tdmrf_txfreq_9','tdmrf_rxfreq_10',
           'tdmrf_txfreq_10','tdmrf_rxfreq_11',
           'tdmrf_txfreq_11','tdmrf_rxfreq_12',
           'tdmrf_txfreq_12','tdmrf_rxfreq_13',
           'tdmrf_txfreq_13','tdmrf_rxfreq_14',
           'tdmrf_txfreq_14','tdmrf_rxfreq_15']

tdma_acm = ['tdmrf_acm', 'tdmrf_mode', 'tdmrf_cn_threshold']

tdma_prot = ['tdmaproto_inroute', 'tdmaproto_slotsnum', 'tdmaproto_slotsize', 'tdmaproto_stations',
             'tdmaproto_not_check_for_stations']

bw_prof = ['tdmabw_active_0', 'tdmabw_idle_0', 'tdmabw_down_0', 'tdmabw_timeout_0', 'tdmabw_active_1',
           'tdmabw_idle_1', 'tdmabw_down_1', 'tdmabw_timeout_1', 'tdmabw_active_2', 'tdmabw_idle_2',
           'tdmabw_down_2', 'tdmabw_timeout_2', 'tdmabw_active_3', 'tdmabw_idle_3', 'tdmabw_down_3',
           'tdmabw_timeout_3', 'tdma_promote_realtime', 'tdma_active_on_traffic', 'tdma_hard_mir_limit',
           'tdma_scaling', 'tdma_new_request_engine']

dyn_net = ['roaming_enabled', 'roaming_time_slots', 'load_balancer_id']

tdma_time = ['tdmatime_mode', 'tdmatime_value']

tlc = ['tlc_enable', 'tlc_maxlvl', 'tlc_netown', 'tlc_avgmin', 'tlc_cnhub', 'tlc_cnremote']
