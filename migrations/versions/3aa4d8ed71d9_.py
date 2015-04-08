"""empty message

Revision ID: 3aa4d8ed71d9
Revises: None
Create Date: 2015-04-08 15:26:18.933404

"""

# revision identifiers, used by Alembic.
revision = '3aa4d8ed71d9'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sense_numbers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('homonym_numbers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('sources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('registers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('domains',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('regions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('origins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('word_classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=30), nullable=True),
    sa.Column('institution', sa.String(length=50), nullable=True),
    sa.Column('country', sa.String(length=50), nullable=True),
    sa.Column('interest', sa.Text(), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('data_sets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('flags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('headwords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('headword', sa.String(length=50), nullable=False),
    sa.Column('definition', sa.Text(), nullable=False),
    sa.Column('see', sa.Text(), nullable=True),
    sa.Column('pronunciation', sa.Text(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('data_set_id', sa.Integer(), nullable=True),
    sa.Column('homonym_number_id', sa.Integer(), nullable=True),
    sa.Column('word_class_id', sa.Integer(), nullable=True),
    sa.Column('sense_number_id', sa.Integer(), nullable=True),
    sa.Column('origin_id', sa.Integer(), nullable=True),
    sa.Column('domain_id', sa.Integer(), nullable=True),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['data_set_id'], ['data_sets.id'], ),
    sa.ForeignKeyConstraint(['domain_id'], ['domains.id'], ),
    sa.ForeignKeyConstraint(['homonym_number_id'], ['homonym_numbers.id'], ),
    sa.ForeignKeyConstraint(['origin_id'], ['origins.id'], ),
    sa.ForeignKeyConstraint(['region_id'], ['regions.id'], ),
    sa.ForeignKeyConstraint(['sense_number_id'], ['sense_numbers.id'], ),
    sa.ForeignKeyConstraint(['word_class_id'], ['word_classes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('citations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=False),
    sa.Column('circa', sa.Boolean(), nullable=True),
    sa.Column('author', sa.String(length=80), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('vol_page', sa.String(length=10), nullable=True),
    sa.Column('edition', sa.String(length=10), nullable=True),
    sa.Column('quote', sa.Text(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['source_id'], ['sources.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('headword_registers',
    sa.Column('headword_id', sa.Integer(), nullable=True),
    sa.Column('register_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['headword_id'], ['headwords.id'], ),
    sa.ForeignKeyConstraint(['register_id'], ['registers.id'], )
    )
    op.create_table('headword_citations',
    sa.Column('headword_id', sa.Integer(), nullable=True),
    sa.Column('citation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['citation_id'], ['citations.id'], ),
    sa.ForeignKeyConstraint(['headword_id'], ['headwords.id'], )
    )
    op.create_table('headword_flags',
    sa.Column('headword_id', sa.Integer(), nullable=True),
    sa.Column('flag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['flag_id'], ['flags.id'], ),
    sa.ForeignKeyConstraint(['headword_id'], ['headwords.id'], )
    )
    op.create_table('citation_source',
    sa.Column('citation_id', sa.Integer(), nullable=True),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['citation_id'], ['citations.id'], ),
    sa.ForeignKeyConstraint(['source_id'], ['sources.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('citation_source')
    op.drop_table('headword_flags')
    op.drop_table('headword_citations')
    op.drop_table('headword_registers')
    op.drop_table('citations')
    op.drop_table('headwords')
    op.drop_table('flags')
    op.drop_table('data_sets')
    op.drop_table('users')
    op.drop_table('word_classes')
    op.drop_table('origins')
    op.drop_table('regions')
    op.drop_table('domains')
    op.drop_table('registers')
    op.drop_table('sources')
    op.drop_table('homonym_numbers')
    op.drop_table('sense_numbers')
    ### end Alembic commands ###
