"""
=========================================================
Atmosphere Model
---------------------------------------------------------
Computes atmospheric properties required by the
fuel estimation model.

Author : HAL Fuel Estimation Project
=========================================================
"""

import math


class AtmosphereModel:

    """
    International Standard Atmosphere (ISA) model.
    """

    SEA_LEVEL_TEMPERATURE_K = 288.15
    LAPSE_RATE = 0.0065

    def isa_temperature(self, altitude_ft: float) -> float:
        """
        Computes ISA temperature at a given altitude.

        Parameters
        ----------
        altitude_ft : float

        Returns
        -------
        float
            Temperature in Kelvin
        """

        altitude_m = altitude_ft * 0.3048

        temperature = (
            self.SEA_LEVEL_TEMPERATURE_K
            - self.LAPSE_RATE * altitude_m
        )

        return temperature

    def temperature_ratio(
        self,
        ambient_temperature_K: float
    ) -> float:
        """
        Computes temperature ratio.

        Returns
        -------
        float
        """

        return math.sqrt(
            ambient_temperature_K /
            self.SEA_LEVEL_TEMPERATURE_K
        )

