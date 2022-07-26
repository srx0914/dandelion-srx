# Copyright 2022 99Cloud, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# flake8: noqa
# fmt: off

"""Add RSU Base Info

Revision ID: 003114bb2d37
Revises: cb28fbd7424f
Create Date: 2022-07-21 14:51:49.064152

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "003114bb2d37"
down_revision = "cb28fbd7424f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("rsu", sa.Column("imei", sa.String(length=64), nullable=True))
    op.add_column("rsu", sa.Column("icc_id", sa.String(length=64), nullable=True))
    op.add_column("rsu", sa.Column("communication_type", sa.String(length=64), nullable=True))
    op.add_column(
        "rsu", sa.Column("running_communication_type", sa.String(length=64), nullable=True)
    )
    op.add_column("rsu", sa.Column("transprotocal", sa.String(length=64), nullable=True))
    op.add_column("rsu", sa.Column("software_version", sa.String(length=64), nullable=True))
    op.add_column("rsu", sa.Column("hardware_version", sa.String(length=64), nullable=True))
    op.add_column("rsu", sa.Column("depart", sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("rsu", "depart")
    op.drop_column("rsu", "hardware_version")
    op.drop_column("rsu", "software_version")
    op.drop_column("rsu", "transprotocal")
    op.drop_column("rsu", "running_communication_type")
    op.drop_column("rsu", "communication_type")
    op.drop_column("rsu", "icc_id")
    op.drop_column("rsu", "imei")
    # ### end Alembic commands ###