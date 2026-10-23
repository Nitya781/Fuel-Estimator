"""
=========================================================
Fuel Flow Model
---------------------------------------------------------
Computes instantaneous fuel flow from
Engine Thrust and Specific Fuel Consumption.

Author : HAL Fuel Estimation Project
=========================================================
"""


class FuelFlowModel:

    """
    Computes instantaneous fuel flow.
    """

    LBS_TO_KG = 0.45359237

    def calculate(self,
                  thrust_lbf: float,
                  sfc: float):

        """
        Parameters
        ----------
        thrust_lbf : float

        sfc : float
            lb / lbf / hr

        Returns
        -------
        dict
        """

        # -------------------------------------
        # Fuel Flow
        # lb/hr
        # -------------------------------------

        fuel_flow_lbs_hr = thrust_lbf * sfc

        # -------------------------------------
        # kg/hr
        # -------------------------------------

        fuel_flow_kg_hr = (
            fuel_flow_lbs_hr
            * self.LBS_TO_KG
        )

        # -------------------------------------
        # kg/min
        # -------------------------------------

        fuel_flow_kg_min = (
            fuel_flow_kg_hr / 60
        )

        # -------------------------------------
        # kg/sec
        # -------------------------------------

        fuel_flow_kg_sec = (
            fuel_flow_kg_hr / 3600
        )

        return {

            "fuel_flow_lbs_hr":
                fuel_flow_lbs_hr,

            "fuel_flow_kg_hr":
                fuel_flow_kg_hr,

            "fuel_flow_kg_min":
                fuel_flow_kg_min,

            "fuel_flow_kg_sec":
                fuel_flow_kg_sec
        }
