package com.example.geradordenumeroreal

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.geradordenumeroreal.databinding.ActivityPrimeiraTelaBinding

class PrimeiraTela : AppCompatActivity() {
    private lateinit var binding: ActivityPrimeiraTelaBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPrimeiraTelaBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.irGerar.setOnClickListener {

            val irGerar = Intent(this, SegundaTela::class.java)
            startActivity(irGerar)

        }

        binding.numerosSalvos.setOnClickListener {

            val numerosSalvos = Intent(this, NumerosSalvos::class.java)
            startActivity(numerosSalvos)

        }

        binding.doacao.setOnClickListener {

            val irDoacao = Intent(this, Doacao::class.java)
            startActivity(irDoacao)

        }

        binding.criptografia.setOnClickListener {

            val criptografia = Intent(this, Criptografia::class.java)
            startActivity(criptografia)

        }

        binding.voltarBnt.setOnClickListener {

            val voltar = Intent(this, MainActivity::class.java)
            startActivity(voltar)
        }
    }
}
